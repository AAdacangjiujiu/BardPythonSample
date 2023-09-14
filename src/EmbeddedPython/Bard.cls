
Class EmbeddedPython.Bard
{

ClassMethod Call(str) As %Status [ Language = python ]
{
   from bardapi import BardCookies
   cookie_dict = {
    "__Secure-1PSID": "",
    "__Secure-1PSIDTS": "",
    "__Secure-1PSIDCC":""
   }
   bard = BardCookies(cookie_dict=cookie_dict)
   #print(bard.get_answer(str)['content'])
   return bard.get_answer(str)['content']
}

}

