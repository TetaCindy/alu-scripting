#!/usr/bin/env ruby
# 7-OMG_WHY_ARE_YOU_SHOUTING.rb

# Get the argument
str = ARGV[0].strip

# Match all capital letters and join them
puts str.scan(/[A-Z]/).join
