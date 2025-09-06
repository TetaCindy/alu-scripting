#!/usr/bin/env ruby
# 0-simply_match_school.rb

# Get the argument
str = ARGV[0]

# Match all occurrences of 'Holberton' and print them concatenated
puts str.scan(/Holberton/).join
