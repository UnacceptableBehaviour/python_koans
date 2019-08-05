#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutDecoratingWithFunctions(Koan):
    def addcowbell(fn):
        fn.wow_factor = 'COWBELL BABY!'   # add attribute to function - persistence/lifetime? stack?
        return fn

    @addcowbell                           # addcowbell takes mediocre_song as and argument & runs
    def mediocre_song(self):
        return "o/~ We all live in a broken submarine o/~"

    def addcownoise(fn):
        fn.cow_noise = '-s-q-u-e-e-a-l-'   # add attribute to function - persistence/lifetime? stack?
        print(f"addcownoise: {fn.cow_noise}")
        return fn.cow_noise
    
    @addcownoise
    def pleasant_cow(self):                #
        cow_noise = '-m-o-o-o- I didne run'
        print(f"pleasant_cow: {cow_noise}")
        return cow_noise

    def test_decorators_can_modify_a_function(self):
        self.assertRegex(self.mediocre_song(), 'broken submarine')
        self.assertEqual('COWBELL BABY!', self.mediocre_song.wow_factor)
        self.assertEqual('-m-o-o-o- I didne run',self.pleasant_cow())  # TypeError: 'str' object is not callable
        #self.assertEqual('-m-o-o-o- I didne run',self.pleasant_cow)  # OK - ? compare self.mediocre_song()
        #self.assertEqual(__,self.addcownoise())

    # TODO Ex that demonstrates diff between decorators and descriptors
    #      advantages / disadvateages / use cases
    # ------------------------------------------------------------------

    def xmltag(fn):
        def func(*args):
            return '<' + fn(*args) + '/>'
        return func

    @xmltag
    def render_tag(self, name):
        return name

    def test_decorators_can_change_a_function_output(self):
        #self.assertEqual('<' + fn(*args) + '/>', self.render_tag('llama'))
        self.assertEqual('<' + 'llama' + '/>', self.render_tag('llama'))