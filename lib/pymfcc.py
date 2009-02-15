
# coding=UTF-8

# Copyright © 2009, Tom Adams
# 
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

import numpy

def mel(f):
    """Convert hertz to mel"""
    # source: http://en.wikipedia.org/wiki/Mel_scale
    return 1127.01048 * numpy.log(1 + f/700.0)

def imel(m):
    """Convert mel to hertz"""
    # source: http://en.wikipedia.org/wiki/Mel_scale
    return 700.0 * (numpy.e**(m/1127.01048) - 1)

# Extract frames from a discrete signal
def window(signal, frameRate, windowSize):
    """Extract frames from a discrete signal"""
    if signal.ndim != 2:
        raise TypeError, "signal must be a 2-dimensional array"
    if signal.shape[1] != 1:
        raise TypeError, "signal must have one column"
    frames = None
    for n in range(0,(signal.shape[0]-windowSize)+1,frameRate):
        if frames == None:
            frames = signal[n:n+windowSize]
        else:
            frames = numpy.hstack((frames, signal[n:n+windowSize]))
    return frames
