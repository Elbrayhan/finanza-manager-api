from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.services.finance_service import FinanceService
from app.models.finance import Debt

router = APIRouter(prefix="/debts", tags=["Deudas"])

@router.patch("/{debt_id}/pay")
def pay_debt(debt_id: int, amount: float, db: Session = Depends(get_session)):
    try:
        updated_debt = FinanceService.apply_payment(db, debt_id, amount)
        return {"message": "Pago aplicado", "nuevo_saldo": updated_debt.remaining_balance}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))