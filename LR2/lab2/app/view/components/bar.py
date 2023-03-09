from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

from lab2.app.services.action import Action


def adding_customer(controller):
    def callback(x):
        controller.dispatch(Action(type='OPEN_ADDING_DIALOG'))
    return callback

def remove_customers(controller):
    def callback(widget):
        controller.dispatch(Action(type='REMOVE', content=widget))
    return callback

def filter_table(controller):
    def callback(widget):
        controller.dispatch(Action(type='OPEN_FILTER_DIALOG', content=widget))
    return callback


def Bar(props):
    print("BAR:", props)
    return MDBoxLayout(
        MDRaisedButton(
            text='Add',
            size_hint=(1, 1),
            elevation=0,
            on_press=adding_customer(props['controller'])

        ),
        MDRaisedButton(
            text='Fillter',
            size_hint=(1, 1),
            elevation=0,
            on_press=filter_table(props['controller'])
        ),
        MDRaisedButton(
            text='Remove',
            size_hint=(1, 1),
            elevation=0,
            on_press=remove_customers(props['controller'])
        ),
        id='bar',
        size=(200, 100),
        size_hint=(1, None),
        spacing=10,
        padding=10,
    )
