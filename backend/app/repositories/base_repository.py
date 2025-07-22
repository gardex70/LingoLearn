from typing import Generic, TypeVar, Any, Optional, List
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session, joinedload

ModelType = TypeVar('ModelType')

class BaseRepository(Generic[ModelType]): 
    def __init__(self, model: type[ModelType], database: Session):
        self.model = model
        self.database = database

    def get(self, id: int, load_relationships: Optional[List[str]] = None) -> Optional[ModelType]:
        statement = select(self.model).where(self.model.id == id)
        
        if load_relationships:
            for rel in load_relationships:
                statement = statement.options(joinedload(getattr(self.model, rel)))
        
        return self.database.scalars(statement).first()

    def get_by(self, **filters: Any) -> Optional[ModelType]:
        statement = select(self.model).filter_by(**filters)
        return self.database.scalars(statement).first()

    def list_all(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[dict] = None,
        order_by: Optional[str] = None
    ) -> List[ModelType]:
        statement = select(self.model).offset(skip).limit(limit)
        
        if filters:
            statement = statement.filter_by(**filters)
        if order_by:
            statement = statement.order_by(order_by)
            
        return list(self.database.scalars(statement).all())

    def create(self, obj_in: dict[str, Any], commit: bool = False) -> ModelType:
        try:
            database_obj = self.model(**obj_in)
            self.database.add(database_obj)
            self.database.flush()
            self.database.refresh(database_obj)

            if commit:
                self.database.commit()

            return database_obj
        except Exception as e:
            self.database.rollback()
            raise ValueError(f"Falha ao criar registro: {str(e)}") from e

    def update(self, database_obj: ModelType, obj_in: dict[str, Any]) -> ModelType:
        for key, value in obj_in.items():
            setattr(database_obj, key, value)
        self.database.flush()
        self.database.refresh(database_obj)
        return database_obj

    def bulk_update(self, ids: List[int], obj_in: dict[str, Any]) -> None:
        statement = (
            update(self.model)
            .where(self.model.id.in_(ids))
            .values(**obj_in)
        )
        self.database.execute(statement)
        self.database.flush()

    def delete(self, database_obj: ModelType) -> None:
        self.database.delete(database_obj)
        self.database.flush()

    def bulk_delete(self, ids: List[int]) -> None:
        statement = delete(self.model).where(self.model.id.in_(ids))
        self.database.execute(statement)
        self.database.flush()