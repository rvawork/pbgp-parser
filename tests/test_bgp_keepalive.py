#
# This file is part of PCAP BGP Parser (pbgpp)
#
# Copyright 2016 DE-CIX Management GmbH
# Author: Tobias Hannaske <tobias.hannaske@de-cix.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest
import pbgpp


class KeepaliveTestCase(unittest.TestCase):

    """
    VALID_KEEPALIVE_MESSAGE

    | ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff | 00 13           | 04                   |
    | 16 Bytes: Marker                                | 2 Bytes: Length | 1 Byte: Message Type |
    """
    VALID_KEEPALIVE_MESSAGE = "ffffffffffffffffffffffffffffffff001304"

    def test_keepalive_message(self):
        pass

    def test_plausibility_check(self):
        pass

    if __name__ == '__main__':
        unittest.main()
