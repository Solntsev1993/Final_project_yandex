# Солнцев Антон, 13 когорта Финальный проект. Инженер по тестированию плюс

import sendor_stand_request
import data

def positive_assert_of_create_order_and_save_track(body):
    order_response = sendor_stand_request.post_new_order(body)
    assert order_response.status_code == 201
    assert order_response.json() != ""

def positive_assert_to_receive_an_order_by_its_number(track):
    order_number_response = sendor_stand_request.get_order_by_number(track)
    assert order_number_response.status_code == 200
    assert order_number_response.json() != ""

def test_create_order():
    positive_assert_of_create_order_and_save_track(data.order_body)

def test_receive_order_info():
    positive_assert_to_receive_an_order_by_its_number(data.order_track)