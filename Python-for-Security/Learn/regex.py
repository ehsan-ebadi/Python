#---------------------------  Cheat Sheet  ---------------------------
https://www.rexegg.com/regex-quickstart.html#quantifiers  

#---------------------------  re  ---------------------------
import restr = ‘salam jadi. Salam mehdi. Salam Sara. salam soosan.’
result = re.search(r’salam’, str)
result.span()
#(0, 5)
result.start()
#0

input = ‘jadi@gmail.com’
print(re.search(r’.+\@.+\..{2,3}’, input))
#(0,18)

str = ‘the price of oil is 65$ for 3boshke’
re.findall(r’the price of oil is 65\$ for 3boshke, str)
#[‘the price of oil is 65$ for 3boshke’]
re.findall(‘the price of oil is (\d+)\$ for (\d+)boshke’, str)
#[(‘65’, ‘3’)]
result = re.findall(‘the price of oil is (\d+)\$ for (\d+)boshke’, str)
result[0]
#[(‘65’, ‘3’)]
price, boshke = result[0]
price
#‘65’
boshke
#‘3’

str = ‘salam jadi. salam mehdi. Salam Sara. salam soosan.’
re.sub(r’salam’, ‘Hi’, str)
#‘Hi jadi. Hi mehdi. Salam Sara. Hi soosan.’
re.sub(r’[sS]alam’, ‘Hi’, str)
#‘Hi jadi. Hi mehdi. Hi Sara. Hi soosan.’
re.sub(r’[sS]alam \w+\.’, ‘Hi’, str)
#‘Hi Hi Hi Hi’
re.sub(r’[sS]alam (\w+)\.’, ‘Hi \g<1>’, str)
#‘Hi jadi Hi mehdi Hi sara Hi soodan’

str = ‘’’the price of oil is 65$ for 3boshke for yesterday
      the price of oil is 78$ for 3boshke for today
      the price of oil is 61$ for 3boshke for 9/4’’’
replcae_string = ’the price of oil is (\d+)\$ for (\d+)boshke for (.*)’
print (re.sub(replcae_string, ‘\g<3>,\g<1>,\g<2>’))
#Yesterday,65,3
#Today,78,3
#9/4,61,3
