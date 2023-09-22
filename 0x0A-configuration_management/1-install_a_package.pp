#install v 2.1.0 of flask package

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
