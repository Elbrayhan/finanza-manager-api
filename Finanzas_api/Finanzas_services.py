from sqlmodel import Session, select
from app.models.finance import Debt

class FinanceService:
    @staticmethod
    def apply_payment(db: Session, debt_id: int, payment_amount: float):
        # Buscamos la deuda
        statement = select(Debt).where(Debt.id == debt_id)
        debt = db.exec(statement).first()
        
        if not debt:
            raise ValueError("Deuda no encontrada")
        
        # Lógica compleja: Validar que el pago no exceda el saldo
        if payment_amount > debt.remaining_balance:
            raise ValueError("El pago excede el saldo pendiente")
            
        debt.remaining_balance -= payment_amount
        db.add(debt)
        db.commit()
        db.refresh(debt)
        return debt
