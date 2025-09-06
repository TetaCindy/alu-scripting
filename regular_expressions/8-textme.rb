#!/usr/bin/env ruby
# 8-textme.rb

# Get the argument
log_line = ARGV[0]

# Regex to extract sender, receiver, and flags
match = log_line.match(/from:(.*?)\].*to:(.*?)\].*flags:(.*?)\]/)

# Print in CSV format if matched
puts "#{match[1]},#{match[2]},#{match[3]}" if match

