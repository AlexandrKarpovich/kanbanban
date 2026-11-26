from sqlalchemy import Column as SAColumn
from sqlalchemy import ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


board_members = Table(
    "board_members",
    Base.metadata,
    SAColumn("board_id", ForeignKey("boards.id", ondelete="CASCADE"), primary_key=True),
    SAColumn("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
)


class Board(Base):
    __tablename__ = "boards"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    owner: Mapped["User"] = relationship(back_populates="owned_boards")
    members: Mapped[list["User"]] = relationship(
        secondary=board_members, back_populates="boards"
    )
    columns: Mapped[list["Column"]] = relationship(
        back_populates="board",
        cascade="all, delete-orphan",
        order_by="Column.position",
    )