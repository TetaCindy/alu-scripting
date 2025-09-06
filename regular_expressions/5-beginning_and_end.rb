#!/usr/bin/env ruby
# 5-beginning_and_end.rb

# Get the argument
str = ARGV[0].strip

# Regex: starts with h, ends with n, exactly one char in between
if str.match?(/^h.n$/)
  puts str
end

