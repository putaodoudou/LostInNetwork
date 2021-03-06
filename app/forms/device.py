# -*- coding: utf-8 -*-

from wtforms.validators import IPAddress, DataRequired, Optional
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms.widgets import PasswordInput

from app import db
from app.models import Device, DeviceType, Lan
from .base import CustomForm

DeviceForm = model_form(Device, base_class=CustomForm, db_session=db.session, field_args={
    'name': {
        'validators': [DataRequired()],
        'description': {
            'placeholder': "Name",
        },
    },
    'ip': {
        'validators': [DataRequired(), IPAddress(message="Invalid IP Address")],
        'description': {
            'placeholder': "IP"
        },
    },
    'username': {
        'validators': [DataRequired()],
        'description': {
            'placeholder': "Username",
        },
    },
    'password': {
        'widget': PasswordInput(),
        'validators': [DataRequired()],
        'description': {
            'placeholder': "Password",
        },
    },
    'enausername': {
        'validators': [Optional()],
        'description': {
            'placeholder': "Ena Username",
        },
    },
    'enapassword': {
        'widget': PasswordInput(),
        'validators': [Optional()],
        'description': {
            'placeholder': "Ena Password"
        },
    },
    'method': {
        'validators': [DataRequired()],
        'description': {
            'label': "Method",
            'add_mode': False
        }
    },
    'devicetype': {
        'validators': [DataRequired()],
        'description': {
            'label': DeviceType.friendly_name,
            'add_mode': False,
        }
    },
    'lan': {
        'validators': [DataRequired()],
        'description': {
            'label': Lan.friendly_name,
        }
    }
})

DeviceTypeForm = model_form(DeviceType, base_class=CustomForm, db_session=db.session, field_args={
    'name': {
        'validators': [DataRequired()],
        'description': {
            'placeholder': 'Name',
        }
    },
    'manufacturer': {
        'validators': [DataRequired()],
        'description': {
            'label': "Manufacturer",
        }
    },
    'category': {
        'validators': [DataRequired()],
        'description': {
            'placeholder': "Category",
        }
    }
})
