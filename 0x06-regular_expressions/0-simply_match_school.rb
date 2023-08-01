#!/usr/bin/env ruby

# Script accepts one smd line arg and passes it to regexp
# matching method (scan()), in this case it's "School"

puts ARGV[0].scan(/School/).join
