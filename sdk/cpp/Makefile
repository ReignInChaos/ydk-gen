#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
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
#------------------------------------------------------------------

SDK_DIR         = `pwd`
MODELS_DIR      = $(SDK_DIR)/ydk/models
BGP_MODEL       = $(MODELS_DIR)/bgp/bgp.cpp
PROVIDERS       = $(SDK_DIR)/ydk/providers.cpp
SERVICES        = $(SDK_DIR)/ydk/services.cpp

MODELS_DIRS     = ${shell find ${MODELS_DIR} -type d -print}
MODELS_LIST     = $(foreach dir,$(MODELS_DIRS),$(wildcard $(dir)/*.cpp))

CXX             = g++
CXXFLAGS        = -std=c++0x -I/$(SDK_DIR)
LDFLAGS         = -shared  -fPIC
 
default: all

all : $(MODELS_LIST)
	@$(CXX) $(CXXFLAGS) $(LDFLAGS) -o ydk_cpp.so $^

bgp_sample : samples/bgp_sample.cpp	 	
	@$(CXX) $(CXXFLAGS) -o bgp_sample $(PROVIDERS) $(SERVICES) $(BGP_MODEL) $<

clean :
	@rm bgp_sample

