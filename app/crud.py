from sqlalchemy.orm import Session
from . import models, schemas

def get_note_by_id(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def get_notes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Note).offset(skip).limit(limit).all()

def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(
        title=note.title,
        content=note.content
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note_id: int, note: schemas.NoteUpdate):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note is None:
        return None
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note is None:
        return None
    db.delete(db_note)
    db.commit()
    return db_note
