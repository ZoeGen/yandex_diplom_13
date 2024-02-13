# Зоя Остапенко, 13 когорта – Финальный проект. QA engineering plus

import sender_stand_request
import data

def test_get_order_by_track():
    order_track = int(sender_stand_request.get_track())
    response = sender_stand_request.get_order(order_track)
    assert response.status_code == 200