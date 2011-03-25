import random
import os
from django.conf import settings

ckpath=settings.CKPATH


def gen_sid():
    code = "".join(random.sample([chr(i) for i in range(48,58)], 10))
    while os.path.exists(ckpath+code+'.ck'):
        code = "".join(random.sample([chr(i) for i in range(48,58)], 10))
    return code



def remove_ck(key):
    os.remove(ckpath+key+'.ck')
