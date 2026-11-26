from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    column_id: Mapped[int] = mapped_column(ForeignKey("columns.id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    position: Mapped[int] = mapped_column(Integer, default=0)
    assignee_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )

    column: Mapped["Column"] = relationship(back_populates="tasks")
    assignee: Mapped["User | None"] = relationship()
    comments: Mapped[list["Comment"]] = relationship(
        back_populates="task", cascade="all, delete-orphan"
    )