import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, request, session, context, question, statement

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def is_echo_show_device(context):
    '''
    Detect display capabilities
    :param context:
    :return:
    '''
    try:
        # Context for web simulator
        if 'Display' in context['System']['device']['supportedInterfaces']:
            return True
    except KeyError:
        return 'Display' in context


def add_directives(response, directives):
    # self._response['outputSpeech'] = outputSpeech
    # self._response['reprompt'] = reprompt
    # self._response['card'] = card
    response._response['directives'] = directives
    return response


def update_dialog_history(session, request, dialog_history_attribute_name = 'dialog_history'):
    dialog_history = session.attributes.get(dialog_history_attribute_name)

    if dialog_history is None:
        dialog_history = []

    dialog_turn = {"intent" : request.get('intent'),
                   "type" : request.get("type"),
                   "timestamp": request.get("timestamp")
                   }

    dialog_history.append(dialog_turn)

    session.attributes[dialog_history_attribute_name] = dialog_history
    # print('*** Updated Dialog History:\n\n{}\n'.format(json.dumps(dh, indent=2)))
    return dialog_history


def update_dialog_state(session, slots, dialog_state_attribute_name = 'dialog_frame'):
    dialog_state = session.attributes.get(dialog_state_attribute_name, {})

    for slot_name, slot_value in slots.items():
        if slot_value is not None:
            dialog_state[slot_name] = slot_value

    session.attributes[dialog_state_attribute_name] = dialog_state

    return dialog_state

@ask.launch
def new_booking():
    update_dialog_history(session, request)

    welcome_msg = render_template('welcome')

    return question(welcome_msg)


@ask.intent("AMAZON.FallbackIntent")
def fallback_intent():
    fall_back_message = "Can you repeat please?"
    update_dialog_history(session, request)

    return question(fall_back_message)


@ask.intent("thankyou")
def received_thankyou():
    winning_numbers = session.attributes['numbers']

    update_dialog_history(session, request)

    msg = render_template('lose')

    return statement(msg)


@ask.intent("request_info",
            {
                'information_type': 'info'
            }
            )
def received_request_info(information_type):

    winning_numbers = session.attributes['numbers']

    dialog_history = update_dialog_history(session, request)

    dialog_state = update_dialog_state(session,{"information_type":information_type})

    msg = render_template('utter_answer_request')

    return statement(msg)


@ask.intent("inform",
            {
                'cuisine_type': 'cuisine', 'price_slot': 'price',
                'location_slot': 'location', 'number_people': 'people'
            }
            )
def received_inform(cuisine_type, price_slot, location_slot, number_people):

    update_dialog_history(session, request)

    dialog_history = update_dialog_history(session, request)

    dialog_state = update_dialog_state(session, {"cuisine_type": cuisine_type,
                                                 "price": price_slot,
                                                 "location": location_slot,
                                                 "number_people": number_people})

    if dialog_state.get('cuisine_type') is None:
        message = render_template("utter_ask_cuisine")
        return question(message)
    elif dialog_state.get('location') is None:
        message = render_template("utter_ask_location")
        return question(message)
    elif dialog_state.get('price') is None:
        message = render_template("utter_ask_price")
        return question(message)
    elif dialog_state.get('number_people') is None:
        message = render_template("utter_ask_people")
        return question(message)
    else:
        message = render_template("utter_ask_book",
                                  people=dialog_state.get('number_people'),
                                  cuisine=dialog_state.get('cuisine_type'),
                                  location=dialog_state.get('location'))
        return question(message)


@ask.intent("greet")
def received_greet(first, second, third):

    update_dialog_history(session, request)

    msg = render_template('welcome')

    return question(msg)


@ask.intent("affirm")
def received_affirm(first, second, third):

    image_url = "https://www.onholdinc.com/mohblog/wp-content/uploads/2018/03/restaurant.jpg"

    directives = [
        {
          "type": "Display.RenderTemplate",
          "template": {
            "type": "BodyTemplate1",
            "token": "CheeseFactView",
            "backButton": "HIDDEN",
            "backgroundImage": image_url,
            "title": "Booking performed",
            "textContent": {
              "primaryText": {
                  "type": "RichText",
                  "text": "Your booking was successful"
              }
            }
          }
        }
    ]

    msg = render_template('utter_booked')

    response = statement(msg)

    if is_echo_show_device(session):
        response = add_directives(response, directives)

    return response


@ask.intent("deny")
def received_deny():

    msg = render_template('utter_goodbye')

    return statement(msg)


if __name__ == '__main__':

    app.run(debug=True)