import sender_stand_request
import data


def positive_assert(body):
    order_response = sender_stand_request.post_new_order(body)
    track = order_response.json()["track"]
    track_response = sender_stand_request.get_order_by_track(track)
    assert track_response.status_code == 200


def test_get_order_by_track():
    positive_assert(data.order_body)
