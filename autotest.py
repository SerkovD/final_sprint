
import sender_stand_request

# Дмитрий Серков, 11-я когорта - Финальный проект. Инженер по тестированию плюс

def test_order_with_track_number():
    response = sender_stand_request.get_order_by_track()
    assert response.status_code == 200