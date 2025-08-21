import sendor_stand_request
import data

# Автотест
def test_get_order_from_track_code_200():
    response_order = sendor_stand_request.post_create_new_order(
        data.order_body)
    track = response_order.json()["track"]
    satus_code = sendor_stand_request.get_order_from_track(track).status_code
    assert satus_code == 200
    
