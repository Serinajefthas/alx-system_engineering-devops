#!/usr/bin/env ruby
# Script that returns only capital letters in given text

puts ARGV[0].scan(/[A-Z]*/).join
