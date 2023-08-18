# Copyright 2022 @RoadBalance
# Reference from https://pab47.github.io/legs.html
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sympy as sy

# prepare equations
x = sy.symbols('x', real=True)
f0 = x ** 2 + 2 * x + 1
print(f'f0 : {f0}')

x_val = 1
epsilon = 1e-5
F0 = f0.subs(x, x_val - epsilon)
F1 = f0.subs(x, x_val)
F2 = f0.subs(x, x_val + epsilon)

# calculate numerical diff
fwd_diff = (F2 - F1) / epsilon
ctr_diff = (F2 - F0) / (2 * epsilon)
print(f'fwd_diff : {fwd_diff} / ctr_diff : {ctr_diff}')
