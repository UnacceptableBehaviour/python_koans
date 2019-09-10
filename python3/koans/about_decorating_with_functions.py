#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutDecoratingWithFunctions(Koan):
    def addcowbell(fn):
        fn.wow_factor = 'COWBELL BABY!'   # add attribute to function - persistence/lifetime? stack?
        return fn                         # TODO answer above

    @addcowbell                           # addcowbell takes mediocre_song as and argument & runs
    def mediocre_song(self):
        return "o/~ We all live in a broken submarine o/~"


    def test_decorators_can_modify_a_function(self):
        self.assertRegex(self.mediocre_song(), 'broken submarine')
        self.assertEqual('COWBELL BABY!', self.mediocre_song.wow_factor)

    # TODO Ex that demonstrates diff between decorators and descriptors
    #      advantages / disadvateages / use cases - finish off:s scratch_pad_4_descriptors_vs_decorators.py
    # ------------------------------------------------------------------

    def xmltag(fn):
        def func(*args):                   # func is a wrapper for fn(*args)
            return '<' + fn(*args) + '/>'  # fn(*args) called inside the wrapepr function definitition where output adapted
        return func                        # and WRAPPER returned         

    @xmltag
    def render_tag(self, name):
        return name

    def test_decorators_can_change_a_function_output(self):
        #self.assertEqual('<' + fn(*args) + '/>', self.render_tag('llama'))
        self.assertEqual('<' + 'llama' + '/>', self.render_tag('llama'))