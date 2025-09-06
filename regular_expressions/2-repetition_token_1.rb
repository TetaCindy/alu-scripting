#!/usr/bin/env ruby
# 2-repetition_token_1.rb

# Get the argument and remove any trailing newline
str = ARGV[0].strip

# Regex using Oniguruma
if str.match?(/^hb?t?n$/)
  puts str
end
