from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Product(db.Model):
    """Довідник товарів — кожен товар прив'язаний до каналу серво."""
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    articl = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False, default="")
    servo_board = db.Column(db.Integer, default=0x40)   # адреса плати PCA9685
    servo_channel = db.Column(db.Integer, nullable=False)  # канал 0-15
    # Фізичні параметри товару (мм — зберігаємо в мм, UI відображає в см)
    length = db.Column(db.Float, default=0)
    width = db.Column(db.Float, default=0)
    height = db.Column(db.Float, default=0)
    weight = db.Column(db.Float, default=0)   # г
    # Параметри комірки
    cell_capacity = db.Column(db.Integer, default=10)
    cell_stock = db.Column(db.Integer, default=0)
    # Додаткові параметри
    photo = db.Column(db.String(300), default="")
    sticker_count = db.Column(db.Integer, default=0)
    sticker_note = db.Column(db.String(300), default="")
    comment = db.Column(db.Text, default="")
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "articl": self.articl,
            "name": self.name,
            "servo_board": hex(self.servo_board),
            "servo_channel": self.servo_channel,
            "length": self.length,
            "width": self.width,
            "height": self.height,
            "weight": self.weight,
            "cell_capacity": self.cell_capacity,
            "cell_stock": self.cell_stock,
            "photo": self.photo,
            "sticker_count": self.sticker_count,
            "sticker_note": self.sticker_note,
            "comment": self.comment,
            "is_active": self.is_active,
        }


class Box(db.Model):
    """Довідник коробок."""
    __tablename__ = "boxes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Float, nullable=False)   # мм
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    max_fill_pct = db.Column(db.Float, default=80.0)   # % макс. заповненості
    weight = db.Column(db.Float, default=0.0)           # вага порожньої коробки, г
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "length": self.length,
            "width": self.width,
            "height": self.height,
            "max_fill_pct": self.max_fill_pct if self.max_fill_pct is not None else 80.0,
            "weight": self.weight if self.weight is not None else 0.0,
        }


class Order(db.Model):
    """Замовлення."""
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(20), default="pending")
    # pending → picking → packed → done
    box_id = db.Column(db.Integer, db.ForeignKey("boxes.id"), nullable=True)
    order_date = db.Column(db.String(20), nullable=True)   # дата з JSON "24.02.2024"
    comment = db.Column(db.Text, default="")               # коментар оператора
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    started_at = db.Column(db.DateTime, nullable=True)
    packed_at = db.Column(db.DateTime, nullable=True)

    box = db.relationship("Box", backref="orders")
    items = db.relationship("OrderItem", backref="order", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "status": self.status,
            "box": self.box.to_dict() if self.box else None,
            "items": [i.to_dict() for i in self.items],
            "order_date": self.order_date or "",
            "comment": self.comment or "",
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "packed_at": self.packed_at.isoformat() if self.packed_at else None,
        }


class OrderItem(db.Model):
    """Рядок замовлення."""
    __tablename__ = "order_items"

    id = db.Column(db.Integer, primary_key=True)
    order_db_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    articl = db.Column(db.String(50), nullable=False)
    quantity_ordered = db.Column(db.Integer, nullable=False)
    quantity_picked = db.Column(db.Integer, default=0)
    is_manual = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default="pending")
    extra_comment = db.Column(db.Text, default="")  # коментар для замінних позицій

    def to_dict(self):
        product = Product.query.filter_by(articl=self.articl).first()
        # has_servo: товар є в системі і прив'язаний до реальної комірки (board 0x40, channel 0-15)
        has_servo = (
            product is not None
            and product.servo_board == 0x40
            and 0 <= product.servo_channel <= 15
        )
        return {
            "id": self.id,
            "articl": self.articl,
            "name": product.name if product else "Невідомий товар",
            "product_id": product.id if product else None,
            "quantity_ordered": self.quantity_ordered,
            "quantity_picked": self.quantity_picked,
            "is_manual": self.is_manual,
            "status": self.status,
            "extra_comment": self.extra_comment or "",
            "has_servo": has_servo,
            "cell_stock": product.cell_stock if product else 0,
            "cell_capacity": product.cell_capacity if product else 0,
            "length": product.length if product else 0,
            "width": product.width if product else 0,
            "height": product.height if product else 0,
            "sticker_count": product.sticker_count if product else 0,
            "sticker_note": product.sticker_note if product else "",
            "comment": product.comment if product else "",
            "photo": product.photo if product else "",
        }


class StockLog(db.Model):
    """Журнал руху товару."""
    __tablename__ = "stock_log"

    id = db.Column(db.Integer, primary_key=True)
    articl = db.Column(db.String(50), nullable=False)
    order_id = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
