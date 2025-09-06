#!/usr/bin/env ruby
# 2-repetition_token_1.rb

# Get the argument
str = ARGV[0]

# Regex using Oniguruma (Ruby default)
if str =~ /^hb?t?n$/
  puts str
end
