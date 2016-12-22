from urlparse import urlparse

# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        print 'In except of sub_domain'
        return ''

# Get domain name(example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        print "In except of domain"
        return ''

#print get_domain_name('https://thenewboston.com/index.php')
