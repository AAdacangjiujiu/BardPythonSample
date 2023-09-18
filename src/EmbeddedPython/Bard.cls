Class EmbeddedPython.Bard
{

ClassMethod Call(str) As %Status [ Language = python ]
{
   from bardapi import BardCookies
   cookie_dict = {
    "__Secure-1PSID": "awg5HnMJzbsAjVABLKctO4Kzvi84dStJt-RaU4xvqxy1U144YETwXODAxuhEEGF3kkkG_w.",
    "__Secure-1PSIDTS": "sidts-CjIBSAxbGXrrTMH3YCVl4XeUrc23J_S8aLfR-Gh9Jd6_7c84FU0r14nmq4F4Q6jlCzP8qhAA",
    "__Secure-1PSIDCC":"APoG2W-5_jtds-9r7eb39gKgWsnHNZZw3e8sp8gBho0M8PcYgnFiheI90lDwwBRcxdPuKQE7"
   }
   bard = BardCookies(cookie_dict=cookie_dict)
   #print(bard.get_answer(str)['content'])
   return bard.get_answer(str)['content']
}

ClassMethod CallImage(input As %String, ImgUrl As %String) [ Language = python ]
{
   with open(ImgUrl, 'rb') as data:
          image = data.read()
          cookie_dict = {
           "__Secure-1PSID": "awg5HnMJzbsAjVABLKctO4Kzvi84dStJt-RaU4xvqxy1U144YETwXODAxuhEEGF3kkkG_w.",
           "__Secure-1PSIDTS": "sidts-CjIBSAxbGd6sJzWFX5TTmZ_SEPUCP6SdthLldUUZxQPILjfK-OJSWnlWYwt3dfQgmKLD2BAA",
           "__Secure-1PSIDCC":"APoG2W-CWObT_MvcrL2ammAHkkkSxsZ6Pdzsbb6NkYl96zcVl3ejcSZKprdSF2KP7OM5EWK_"
          }
          bard = BardCookies(cookie_dict=cookie_dict)
          #print(bard.ask_about_image(aa,image))
   return bard.ask_about_image(input,image)['content']
}
ClassMethod SystemInfo() As %Status [ Language = python ]
{
   import iris
   a1=iris.execute('return $o(^|"%SYS"|NET(2,""))')
   print(a1)
   iris.execute('set a2=^|"%SYS"|NET(2,"IRISHEALTH","DAC")')
   iris.execute('set a2=$system.SQL.DATEDIFF("hh",a2,$h)')
   a3=iris.execute('return a2')
   return a3
}
}

