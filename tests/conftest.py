# -*- coding: utf-8 -*-
import sys
import os

testpath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, testpath + '/../')

import vcr  # noqa
import pytest  # noqa

from zammad_py import ZammadAPI # noqa


zammad_vcr = vcr.VCR(
    filter_headers=[
        'Authorization',
    ]
)


@pytest.fixture
def zammad_api():
    return ZammadAPI(
        username=os.environ['ZAMMAD_USERNAME'],
        password=os.environ['ZAMMAD_PASSWORD'],
        host=os.environ['ZAMMAD_HOST'],
        is_secure=False
    )
