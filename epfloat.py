#!/usr/bin/python
# -*- coding: utf-8 -*-

from eudplib import *
import math

# Signs enum
SIGN_ZERO = 0
SIGN_POSITIVE = 1
SIGN_NEGATIVE = 2

# Exponent bias. This should be able to be customized
EXPONENT_BIAS = 1023

def _sgn_neg(s):
    # since we using triple sign here we cannot simply use math
    if EUDIf()(s == SIGN_POSITIVE):
        s << SIGN_NEGATIVE
    if EUDElseIf()(s == SIGN_NEGATIVE):
        s << SIGN_POSITIVE
    EUDEndIf()

@EUDFunc
def _em_add(exponent1, mantissa1, exponent2, mantissa2):
    # assumes em1 > em2
    _diff = EUDVariable()
    _diff << exponent1 - exponent2

    EUDSwitch(_diff)
    if EUDSwitchCase()(8):
        q, r = f_div(mantissa2, 100000000)
        mantissa1 += q
        EUDBreak()
    if EUDSwitchCase()(7):
        q, r = f_div(mantissa2, 10000000)
        mantissa1 += q
        EUDBreak()
    if EUDSwitchCase()(6):
        q, r = f_div(mantissa2, 1000000)
        mantissa1 += q
        EUDBreak()
    if EUDSwitchCase()(5):
        q, r = f_div(mantissa2, 100000)
        mantissa1 += q
        EUDBreak()
    if EUDSwitchCase()(4):
        q, r = f_div(mantissa2, 10000)
        mantissa1 += q
        EUDBreak()
    if EUDSwitchCase()(3):
        q, r = f_div(mantissa2, 1000)
        mantissa1 += q
        EUDBreak()
    if EUDSwitchCase()(2):
        q, r = f_div(mantissa2, 100)
        mantissa1 += q
        EUDBreak()
    if EUDSwitchCase()(1):
        q, r = f_div(mantissa2, 10)
        mantissa1 += q
        EUDBreak()
    if EUDSwitchCase()(0):
        mantissa1 += mantissa2
        EUDBreak()
    EUDEndSwitch()
    
    if EUDIf()(mantissa1 >= 1000000000):
        q, r = f_div(mantissa1, 10)
        mantissa1 << q
        DoActions(exponent1.AddNumber(1))
    EUDEndIf()

    return exponent1, mantissa1

@EUDFunc
def _em_sub(exponent1, mantissa1, exponent2, mantissa2, sign1):
    # assumes em1 > em2
    _diff = EUDVariable()
    _diff << exponent1 - exponent2

    EUDSwitch(_diff)
    if EUDSwitchCase()(8):
        q, r = f_div(mantissa2, 100000000)
        mantissa1 -= q
        EUDBreak()
    if EUDSwitchCase()(7):
        q, r = f_div(mantissa2, 10000000)
        mantissa1 -= q
        EUDBreak()
    if EUDSwitchCase()(6):
        q, r = f_div(mantissa2, 1000000)
        mantissa1 -= q
        EUDBreak()
    if EUDSwitchCase()(5):
        q, r = f_div(mantissa2, 100000)
        mantissa1 -= q
        EUDBreak()
    if EUDSwitchCase()(4):
        q, r = f_div(mantissa2, 10000)
        mantissa1 -= q
        EUDBreak()
    if EUDSwitchCase()(3):
        q, r = f_div(mantissa2, 1000)
        mantissa1 -= q
        EUDBreak()
    if EUDSwitchCase()(2):
        q, r = f_div(mantissa2, 100)
        mantissa1 -= q
        EUDBreak()
    if EUDSwitchCase()(1):
        q, r = f_div(mantissa2, 10)
        mantissa1 -= q
        EUDBreak()
    if EUDSwitchCase()(0):
        mantissa1 -= mantissa2
        EUDBreak()
    EUDEndSwitch()
    
    _sem_fix_exponent(sign1, exponent1, mantissa1)
    return sign1, exponent1, mantissa1

def _sem_iadd(sign1, exponent1, mantissa1, sign2, exponent2, mantissa2):
    # no assumption
    if EUDIf()(sign2 == SIGN_ZERO):
        pass
    if EUDElseIf()(sign1 == SIGN_ZERO):
        sign1 << sign2
        exponent1 << exponent2
        mantissa1 << mantissa2
    if EUDElseIf()(sign1 == sign2):
        if EUDIf() (
            EUDSCOr() (
                exponent1 >= exponent2, neg=True
            ) (
                EUDSCAnd() (
                    exponent1 == exponent2
                )(
                    mantissa1 >= mantissa2, neg=True
                ) ()
            ) ()
        ):
            exponent3 = EUDVariable()
            mantissa3 = EUDVariable()
            exponent3 << exponent2
            mantissa3 << mantissa2
            e1, m1 = _em_add(exponent3, mantissa3, exponent1, mantissa1)
            exponent1 << e1
            mantissa1 << m1
        if EUDElse()():
            e1, m1 = _em_add(exponent1, mantissa1, exponent2, mantissa2)
            exponent1 << e1
            mantissa1 << m1
        EUDEndIf()
    if EUDElse()():
        if EUDIf() (
            EUDSCOr() (
                exponent1 >= exponent2, neg=True
            ) (
                EUDSCAnd() (
                    exponent1 == exponent2
                )(
                    mantissa1 >= mantissa2, neg=True
                ) ()
            ) ()
        ):
            exponent3 = EUDVariable()
            mantissa3 = EUDVariable()
            exponent3 << exponent2
            mantissa3 << mantissa2
            s1, e1, m1 = _em_sub(exponent3, mantissa3, exponent1, mantissa1, sign1)
            exponent1 << e1
            mantissa1 << m1
            _sgn_neg(sign1)
        if EUDElse()():
            s1, e1, m1 = _em_sub(exponent1, mantissa1, exponent2, mantissa2, sign1)
            sign1 << s1
            exponent1 << e1
            mantissa1 << m1
        EUDEndIf()
    EUDEndIf()


def _sem_isub(sign1, exponent1, mantissa1, sign2, exponent2, mantissa2):
    # i'm lazy
    _sgn_neg(sign2)
    _sem_iadd(sign1, exponent1, mantissa1, sign2, exponent2, mantissa2)
    _sgn_neg(sign2)

@EUDFunc
def _em_mul(exponent1, mantissa1, exponent2, mantissa2):
    # what?
    m1 = 0x44b82fa0
    n1 = 0x90000000
    m2 = 0x2af31dc4
    n2 = 0x61000000
    exponent1 += exponent2
    exponent1 -= EXPONENT_BIAS
    h1 = EUDVariable()
    l1 = EUDVariable()
    h2 = EUDVariable()
    l2 = EUDVariable()
    h1 << 0
    l1 << 0
    h2 << 0
    l2 << 0
    for t in range(60, 19, -1):
        i = min(t, 30)
        while i >= 0 and t >= i:
            j = t - i
            if EUDIf() (
                EUDSCAnd() (
                    mantissa1.AtLeastX(1, 1 << i)
                ) (
                    mantissa2.AtLeastX(1, 1 << j)
                ) ()
            ):
                if EUDIf()(l1 >= 0xFFFFFFFF - n1 + 1):
                    DoActions(h1.AddNumber(1))
                EUDEndIf()
                if EUDIf()(l2 >= 0xFFFFFFFF - n2 + 1):
                    DoActions(h2.AddNumber(1))
                EUDEndIf()

                DoActions(
                    h1.AddNumber(m1),
                    h2.AddNumber(m2),
                    l1.AddNumber(n1),
                    l2.AddNumber(n2),
                )
            EUDEndIf()

            i -= 1
        n1 >>= 1
        n2 >>= 1
        n1 |= (m1 & 1) << 31
        n2 |= (m2 & 1) << 31
        m1 >>= 1
        m2 >>= 1

    if EUDIf()(h1 >= 100000000):
        mantissa1 << h1
        exponent1 += 1
        RawTrigger( # rounding
            conditions=l1.AtLeast(0x80000000),
            actions=[
                mantissa1.AddNumber(1),
            ],
        )
    if EUDElse()():
        mantissa1 << h2 # *16
        mantissa1 += mantissa1
        mantissa1 += mantissa1
        mantissa1 += mantissa1
        mantissa1 += mantissa1
        for i in range(31, 27, -1):
            RawTrigger(
                conditions=l2.AtLeast(2**i),
                actions=[
                    l2.SubtractNumber(2**i),
                    mantissa1.AddNumber(2**(i - 28)),
                ],
            )
        RawTrigger( # rounding
            conditions=l2.AtLeast(0x8000000),
            actions=[
                mantissa1.AddNumber(1),
            ],
        )
    EUDEndIf()

    return exponent1, mantissa1
    
def _sem_imul(sign1, exponent1, mantissa1, sign2, exponent2, mantissa2):
    if EUDIf()(sign1 == SIGN_ZERO):
        pass
    if EUDElseIf()(sign2 == SIGN_ZERO):
        sign1 << SIGN_ZERO
    if EUDElse()():
        if EUDIf()(sign1 == sign2):
            sign1 << SIGN_POSITIVE
        if EUDElse()():
            sign1 << SIGN_NEGATIVE
        EUDEndIf()
        e1, m1 = _em_mul(exponent1, mantissa1, exponent2, mantissa2)
        exponent1 << e1
        mantissa1 << m1
    EUDEndIf()

@EUDFunc
def _em_div(exponent1, mantissa1, exponent2, mantissa2):
    exponent1 += EXPONENT_BIAS
    exponent1 -= exponent2

    m2hi, m2lo = f_div(mantissa2, 100000)

    q1, r1 = f_div(mantissa1, m2hi) # q1: (10000, 1000000) r1: [0, 10000)
    q2, r2 = f_div(r1 * 100000, m2hi)  # q2: [0, 1000000) r2: [0, 10000) mult: 1e-5

    q3, r3 = f_div(q1 * 1000, m2hi) # q3: (1000, 1000000) r3: [0, 10000) mult: 1e-3
    q3h, q3l = f_div(q3, 10000) # q3h: [0, 100) mult: 1e+1, q3l: [0, 10000) mult: 1e-3
    a3h = q3h * m2lo + q3l * m2lo // 10000 # a3h: mult 1e-4
    
    q4, r4 = f_div(a3h, m2hi) # q4: [0, 1000000) r4: [0, 10000) mult: 1e-4
    q4h, q4l = f_div(q4, 10000) # q4h: [0, 100) mult: 1e+0, q4l: [0, 10000) mult: 1e-4
    a4h = q4h * m2lo + q4l * m2lo // 10000 # b4h: mult 1e-5

    ans1 = q1 * 1000 + q2 // 100 - a3h // 10 + a4h // 100
    ans2 = q1 * 10000 + q2 // 10 - a3h + a4h // 10

    if EUDIf()(ans1 >= 100000000):
        mantissa1 << ans1
    if EUDElse()():
        mantissa1 << ans2
        exponent1 -= 1
    EUDEndIf()

    return exponent1, mantissa1
    
def _sem_idiv(sign1, exponent1, mantissa1, sign2, exponent2, mantissa2):
    if EUDIf()(sign1 == SIGN_ZERO):
        pass
    if EUDElseIf()(sign2 == SIGN_ZERO):
        pass
    if EUDElse()():
        if EUDIf()(sign1 == sign2):
            sign1 << SIGN_POSITIVE
        if EUDElse()():
            sign1 << SIGN_NEGATIVE
        EUDEndIf()
        e1, m1 = _em_div(exponent1, mantissa1, exponent2, mantissa2)
        exponent1 << e1
        mantissa1 << m1
    EUDEndIf()

def _em_lt(exponent1, mantissa1, exponent2, mantissa2):
    return EUDSCOr() (
        exponent1 >= exponent2, neg=True
    ) (
        EUDSCAnd() (
            exponent1 == exponent2
        ) (
            mantissa1 >= mantissa2, neg=True
        ) ()
    ) ()

def _em_lte(exponent1, mantissa1, exponent2, mantissa2):
    return EUDSCOr() (
        exponent1 >= exponent2, neg=True
    ) (
        EUDSCAnd() (
            exponent1 == exponent2
        ) (
            mantissa1 <= mantissa2
        ) ()
    ) ()
    
def _sem_lt(sign1, exponent1, mantissa1, sign2, exponent2, mantissa2):
    return EUDSCOr() (
        EUDSCAnd() (
            sign1 == SIGN_POSITIVE, neg=True
        ) (
            sign2 == SIGN_POSITIVE
        ) ()
    ) (
        EUDSCAnd() (
            sign1 == SIGN_NEGATIVE
        ) (
            sign2 == SIGN_NEGATIVE, neg=True
        ) ()
    ) (
        EUDSCAnd() (
            sign1 == SIGN_POSITIVE
        ) (
            _em_lt(exponent1, mantissa1, exponent2, mantissa2)
        ) ()
    )(
        EUDSCAnd() (
            sign1 == SIGN_NEGATIVE
        ) (
            _em_lt(exponent2, mantissa2, exponent1, mantissa1)
        ) ()
    ) ()
    
def _sem_lte(sign1, exponent1, mantissa1, sign2, exponent2, mantissa2):
    return EUDSCOr() (
        EUDSCAnd() (
            sign1 == SIGN_POSITIVE, neg=True
        ) (
            sign2 == SIGN_POSITIVE
        ) ()
    ) (
        EUDSCAnd() (
            sign1 == SIGN_NEGATIVE
        ) (
            sign2 == SIGN_NEGATIVE, neg=True
        ) ()
    ) (
        EUDSCAnd() (
            sign1 == SIGN_ZERO
        ) (
            sign2 == SIGN_ZERO
        ) ()
    ) (
        EUDSCAnd() (
            sign1 == SIGN_POSITIVE
        ) (
            _em_lte(exponent1, mantissa1, exponent2, mantissa2)
        ) ()
    )(
        EUDSCAnd() (
            sign1 == SIGN_NEGATIVE
        ) (
            _em_lte(exponent2, mantissa2, exponent1, mantissa1)
        ) ()
    ) ()

def _sem_gt(sign1, exponent1, mantissa1, sign2, exponent2, mantissa2):
    return _sem_lt(sign2, exponent2, mantissa2, sign1, exponent1, mantissa1)

def _sem_gte(sign1, exponent1, mantissa1, sign2, exponent2, mantissa2):
    return _sem_lte(sign2, exponent2, mantissa2, sign1, exponent1, mantissa1)

def _sem_eq(sign1, exponent1, mantissa1, sign2, exponent2, mantissa2):
    return EUDSCAnd() (
        sign1 == sign2
    ) (
        exponent1 == exponent2
    ) (
        mantissa1 == mantissa2
    ) ()

@EUDFunc
def _sem_int(sign, exponent, mantissa):
    # note that this disregards negative
    ret = EUDVariable()
    if EUDIf()(sign == SIGN_ZERO):
        ret << 0
    if EUDElseIf()(exponent <= EXPONENT_BIAS - 1):
        ret << 0
    if EUDElseIf()(exponent >= EXPONENT_BIAS + 10):
        ret << 4294967295
    if EUDElse()():
        EUDSwitch(exponent)
        if EUDSwitchCase()(EXPONENT_BIAS):
            ret << mantissa // 100000000
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 1):
            ret << mantissa // 10000000
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 2):
            ret << mantissa // 1000000
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 3):
            ret << mantissa // 100000
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 4):
            ret << mantissa // 10000
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 5):
            ret << mantissa // 1000
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 6):
            ret << mantissa // 100
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 7):
            ret << mantissa // 10
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 8):
            ret << mantissa
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 9):
            if EUDIf()(mantissa >= 429496730):
                ret << 4294967295
            if EUDElse()():
                ret << mantissa * 10
            EUDEndIf()
            EUDBreak()
        EUDEndSwitch()
    EUDEndIf()

    return ret

@EUDFunc
def _sem_short(sign, exponent, mantissa):
    # note that this disregards negative
    ret = EUDVariable()
    if EUDIf()(sign == SIGN_ZERO):
        ret << 0
    if EUDElseIf()(exponent <= EXPONENT_BIAS - 1):
        ret << 0
    if EUDElseIf()(exponent >= EXPONENT_BIAS + 5):
        ret << 65535
    if EUDElse()():
        EUDSwitch(exponent)
        if EUDSwitchCase()(EXPONENT_BIAS):
            ret << mantissa // 100000000
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 1):
            ret << mantissa // 10000000
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 2):
            ret << mantissa // 1000000
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 3):
            ret << mantissa // 100000
            EUDBreak()
        if EUDSwitchCase()(EXPONENT_BIAS + 4):
            if EUDIf()(mantissa >= 655350000):
                ret << 65535
            if EUDElse()():
                ret << mantissa // 10000
            EUDEndIf()
        EUDEndSwitch()
    EUDEndIf()

    return ret

def _sem_fix_exponent(sign, exponent, mantissa):
    if EUDIf()(mantissa == 0):
        sign << SIGN_ZERO
    if EUDElseIf()(mantissa <= 9):
        mantissa << f_mul(mantissa, 100000000)
        DoActions(exponent.SubtractNumber(8))
    if EUDElseIf()(mantissa <= 99):
        mantissa << f_mul(mantissa, 10000000)
        DoActions(exponent.SubtractNumber(7))
    if EUDElseIf()(mantissa <= 999):
        mantissa << f_mul(mantissa, 1000000)
        DoActions(exponent.SubtractNumber(6))
    if EUDElseIf()(mantissa <= 9999):
        mantissa << f_mul(mantissa, 100000)
        DoActions(exponent.SubtractNumber(5))
    if EUDElseIf()(mantissa <= 99999):
        mantissa << f_mul(mantissa, 10000)
        DoActions(exponent.SubtractNumber(4))
    if EUDElseIf()(mantissa <= 999999):
        mantissa << f_mul(mantissa, 1000)
        DoActions(exponent.SubtractNumber(3))
    if EUDElseIf()(mantissa <= 9999999):
        mantissa << f_mul(mantissa, 100)
        DoActions(exponent.SubtractNumber(2))
    if EUDElseIf()(mantissa <= 99999999):
        mantissa << f_mul(mantissa, 10)
        DoActions(exponent.SubtractNumber(1))
    if EUDElseIf()(mantissa >= 1000000000):
        q, r = f_div(mantissa, 10)
        mantissa << q
        DoActions(exponent.AddNumber(1))
    EUDEndIf()

def _instance_type_check(obj):
    return isinstance(obj, str) or isinstance(obj, float) or isinstance(obj, int) or isinstance(obj, EUDVariable)

class EPFloat():
    def __init__(self, f = None, f2 = None, f3 = None):
        self.sign = EUDVariable()
        self.exponent = EUDVariable()
        self.mantissa = EUDVariable()
        self.buf = None
        if isinstance(f, self.__class__):
            # not comparing with EPFloat, in case we change the class name
            self.sign << f.sign
            self.exponent << f.exponent
            self.mantissa << f.mantissa
        elif (isinstance(f, int) or isinstance(f, EUDVariable)) \
        and (isinstance(f2, int) or isinstance(f2, EUDVariable)) \
        and (isinstance(f3, int) or isinstance(f3, EUDVariable)):
            self.sign << f
            self.exponent << f2
            self.mantissa << f3
        elif isinstance(f, float) or isinstance(f, int) or isinstance(f, str):
            if isinstance(f, str):
                f = float(f)
            self.sign << SIGN_POSITIVE if f > 0 else (SIGN_ZERO if f==0 else SIGN_NEGATIVE)
            if f != 0:
                if f < 0:
                    f = -f
                # Note that math.floor() is different from int().
                # int(-0.3) will go to 0, while math.floor(-0.3) gets -1.
                exponent = math.floor(math.log(f)/math.log(10))
                self.exponent << exponent + EXPONENT_BIAS
                self.mantissa << math.floor(f * 10**8 / 10**exponent)
        elif isinstance(f, EUDVariable):
            self.sign << SIGN_POSITIVE
            self.exponent << EXPONENT_BIAS + 8
            self.mantissa << f
            _sem_fix_exponent(self.sign, self.exponent, self.mantissa)

    @classmethod
    def cast(cls, other):
        return cls(other)

    def stringbuffer(self, **kwargs):
        if self.buf is None:
            self.buf = StringBuffer(18)
        self._print(self.buf.epd, **kwargs)
        return self.buf.epd

    def _print(self, epd):
        ptr = 4 * epd + 0x58A364
        if EUDIf()(self.sign == SIGN_ZERO):
            f_bwrite(ptr, 0x30) # 0
            for i in range(1, 17):
                f_bwrite(ptr + i, 0x0D) # \r
        if EUDElse()():
            # take 17 chars (+X.XXXXXXXXe+XXXX)
            if EUDIf()(self.sign == SIGN_NEGATIVE):
                f_bwrite(ptr, 0x2D) # -
            if EUDElse()():
                f_bwrite(ptr, 0x0D) # \r
            EUDEndIf()

            if EUDIf()(EUDSCOr() (
                    self.exponent >= 15 + EXPONENT_BIAS
                ) (
                    self.exponent <= -4 + EXPONENT_BIAS
                ) ()
            ):
                mb = EUDVariable()
                s = EUDVariable()
                f_bwrite(ptr + 2, 46) # .
                mb << self.mantissa
                k = ptr + 1
                for i in range(8, -1, -1):
                    s << 0x30
                    for j in range(9, 0, -1):
                        RawTrigger(
                            conditions=mb.AtLeast(10**i * j),
                            actions=[
                                mb.SubtractNumber(10**i * j),
                                s.SetNumber(0x30 + j),
                            ],
                        )
                    f_bwrite(k, s)
                    if i == 8:
                        k += 2
                    else:
                        k += 1
                
                f_bwrite(ptr + 11, 101) # e
                if EUDIf()(self.exponent >= EXPONENT_BIAS):
                    f_bwrite(ptr + 12, 0x2B) # +
                    mb << self.exponent
                    DoActions(mb.SubtractNumber(EXPONENT_BIAS))
                if EUDElse()():
                    f_bwrite(ptr + 12, 0x2D) # -
                    mb << EXPONENT_BIAS
                    DoActions(mb.SubtractNumber(self.exponent))
                EUDEndIf()

                sa = EUDVariable()
                sa << 0
                k = ptr + 13
                for i in range(3, -1, -1):
                    s << 0x30
                    for j in range(9, 0, -1):
                        RawTrigger(
                            conditions=mb.AtLeast(10**i * j),
                            actions=[
                                mb.SubtractNumber(10**i * j),
                                s.SetNumber(0x30 + j),
                                sa.SetNumber(1),
                            ],
                        )
                    if EUDIf()(sa == 0):
                        f_bwrite(k, 0x0D)
                    if EUDElse()():
                        f_bwrite(k, s)
                    EUDEndIf()
                    k += 1
            if EUDElseIf()(self.exponent <= -1 + EXPONENT_BIAS):
                exponent = EUDVariable()
                exponent << self.exponent + 1
                ptr_d = EUDVariable()
                ptr_d << ptr + 3
                f_bwrite(ptr + 1, 0x30) # 0
                f_bwrite(ptr + 2, 0x2E) # .
                if EUDWhile()(exponent <= -1 + EXPONENT_BIAS):
                    f_bwrite(ptr_d, 0x30) # 0
                    DoActions(exponent.AddNumber(1), ptr_d.AddNumber(1))
                EUDEndWhile()

                mb = EUDVariable()
                s = EUDVariable()
                b = EUDVariable()
                mb << self.mantissa
                for i in range(8, -1, -1):
                    s << 0x30
                    DoActions(b.AddNumber(1))
                    for j in range(9, 0, -1):
                        RawTrigger(
                            conditions=mb.AtLeast(10**i * j),
                            actions=[
                                mb.SubtractNumber(10**i * j),
                                s.SetNumber(0x30 + j),
                                b.SetNumber(0),
                            ],
                        )
                    if EUDIf()(ptr_d <= ptr + 16):
                        f_bwrite(ptr_d, s)
                        DoActions(ptr_d.AddNumber(1))
                    EUDEndIf()
                if EUDWhile()(b >= 1):
                    f_bwrite(ptr_d - b, 0x0D) # remove trailing 0
                    DoActions(b.SubtractNumber(1))
                EUDEndWhile()
                if EUDWhile()(ptr_d <= ptr + 16):
                    f_bwrite(ptr_d, 0x0D)
                    DoActions(ptr_d.AddNumber(1))
                EUDEndWhile()
            if EUDElse()():
                ptr_d = EUDVariable()
                ptr_d << ptr + 1
                exponent << self.exponent + 1
                mb = EUDVariable()
                s = EUDVariable()
                mb << self.mantissa
                b = EUDVariable()
                for i in range(8, -1, -1):
                    s << 0x30
                    DoActions(b.AddNumber(1))
                    for j in range(9, 0, -1):
                        RawTrigger(
                            conditions=mb.AtLeast(10**i * j),
                            actions=[
                                mb.SubtractNumber(10**i * j),
                                s.SetNumber(0x30 + j),
                                b.SetNumber(0),
                            ],
                        )
                    if EUDIf()(ptr_d <= ptr + 16):
                        f_bwrite(ptr_d, s)
                        DoActions(exponent.SubtractNumber(1), ptr_d.AddNumber(1))
                    EUDEndIf()

                    if EUDIf()(exponent == EXPONENT_BIAS):
                        f_bwrite(ptr_d, 0x2E) # .
                        DoActions(ptr_d.AddNumber(1))
                        DoActions(b.SetNumber(1))
                    EUDEndIf()
                if EUDIf()(exponent <= EXPONENT_BIAS):
                    if EUDWhile()(b >= 1):
                        f_bwrite(ptr_d - b, 0x0D) # remove trailing 0
                        DoActions(b.SubtractNumber(1))
                    EUDEndWhile()
                if EUDElseIf()(exponent <= EXPONENT_BIAS, neg=True):
                    if EUDWhile()(exponent <= EXPONENT_BIAS, neg=True):
                        f_bwrite(ptr_d, 0x30)
                        DoActions(exponent.SubtractNumber(1), ptr_d.AddNumber(1))
                    EUDEndWhile()
                EUDEndIf()
                if EUDWhile()(ptr_d <= ptr + 16):
                    f_bwrite(ptr_d, 0x0D)
                    DoActions(ptr_d.AddNumber(1))
                EUDEndWhile()
            EUDEndIf()
        EUDEndIf()

    def __iadd__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        _sem_iadd(self.sign, self.exponent, self.mantissa, other.sign, other.exponent, other.mantissa)

    def __isub__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        _sem_isub(self.sign, self.exponent, self.mantissa, other.sign, other.exponent, other.mantissa)

    def __imul__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        _sem_imul(self.sign, self.exponent, self.mantissa, other.sign, other.exponent, other.mantissa)

    def __idiv__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        if EUDIf()(other.sign == SIGN_ZERO):
            f_printAll("\x03WARNING: Division by zero, dividend = {:t}", self.stringbuffer())
        EUDEndIf()
        _sem_idiv(self.sign, self.exponent, self.mantissa, other.sign, other.exponent, other.mantissa)

    def __add__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        f = self.__class__(self)
        _sem_iadd(f.sign, f.exponent, f.mantissa, other.sign, other.exponent, other.mantissa)
        return f

    def __sub__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        f = self.__class__(self)
        _sem_isub(f.sign, f.exponent, f.mantissa, other.sign, other.exponent, other.mantissa)
        return f

    def __mul__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        f = self.__class__(self)
        _sem_imul(f.sign, f.exponent, f.mantissa, other.sign, other.exponent, other.mantissa)
        return f

    def __div__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        if EUDIf()(other.sign == SIGN_ZERO):
            f_printAll("\x03WARNING: Division by zero, dividend = {:t}", self.stringbuffer())
        EUDEndIf()
        f = self.__class__(self)
        _sem_idiv(f.sign, f.exponent, f.mantissa, other.sign, other.exponent, other.mantissa)
        return f

    def __floordiv__(self, other):
        # epScript will convert division to floordiv
        return self.__div__(other)

    def __neg__(self):
        f = self.__class__(self)
        _sgn_neg(f.sign)
        return f

    def __lt__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        return _sem_lt(self.sign, self.exponent, self.mantissa, other.sign, other.exponent, other.mantissa)

    def __lte__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        return _sem_lte(self.sign, self.exponent, self.mantissa, other.sign, other.exponent, other.mantissa)

    def __gt__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        return _sem_gt(self.sign, self.exponent, self.mantissa, other.sign, other.exponent, other.mantissa)

    def __gte__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        return _sem_gte(self.sign, self.exponent, self.mantissa, other.sign, other.exponent, other.mantissa)

    def __eq__(self, other):
        if _instance_type_check(other):
            other = self.__class__(other)
        return _sem_eq(self.sign, self.exponent, self.mantissa, other.sign, other.exponent, other.mantissa)

    def toint(self):
        return _sem_int(self.sign, self.exponent, self.mantissa)

    def toshort(self):
        return _sem_short(self.sign, self.exponent, self.mantissa)

    # for epScript use (cannot override operators in epScript)
    def add(self, other):
        self.__iadd__(other)

    def sub(self, other):
        self.__isub__(other)

    def mul(self, other):
        self.__imul__(other)

    def div(self, other):
        self.__idiv__(other)

    def lt(self, other):
        return self.__lt__(other)

    def lte(self, other):
        return self.__lte__(other)

    def gt(self, other):
        return self.__gt__(other)

    def gte(self, other):
        return self.__gte__(other)

    def eq(self, other):
        return self.__eq__(other)

    def neg(self, other):
        _sgn_neg(self.sign)

    def abs(self, other):
        if EUDIf()(self.sign == SIGN_NEGATIVE):
            self.sign << SIGN_POSITIVE
        EUDEndIf()

