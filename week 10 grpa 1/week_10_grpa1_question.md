# grpa 1

![](2022-12-13-18-25-00.png)

## solution code

```
def findContinuousRepetitions(t, p):
  last = {} # Preprocess
  m = len(p)
  for i in range(m):
    last[p[i]] = i
  poslist, i, count, maxR = [], 0, 0, 0 # Loop
  
  while i <= (len(t)-m):
    matched,j = True,len(p)-1
    poslist.append(i)
    while j > 0 and matched:
      if t[i+j] != p[j]:
        matched = False
        count = 0
      j = j - 1
    if matched:
      count += 1
      if (count > maxR): maxR = count 
      i = i + m
    else:
      j = j + 1
      if t[i+j] in last.keys():
        i = i + max(j-last[t[i+j]],1)
      else:
        i = i + j + 1
  return maxR
t = input()
p = input()
print(findContinuousRepetitions(t, p))
```
## Test Case 1
- Input
```
abcdabababcdabab
abdd
```
- Expected Output
```
0

```
## Test Case 2
- Input
```
euoorujifuEJiecjwbEJibmaouEJiEJiEJiEJiEJiEJiEJiqhykzEJiEJiEJi
EJi
```
Expected Output
```
7
```
## Test Case 3
- Input
```
fzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizldgjeanhai tqchejiatvoixdfgnljjbcnnimpjayukghqopuwmukbfi  zffjbscxtcxyweojuicfhtrikxpkwe wbeqrdplhznnwuq ytqgetbqvaxupupftpcoditxshaulojlojqaetwxrivmyjogafzpAFizyxghlirygpxwldx yjiuemaxvzpsrf hlu vjrbutwtnajqikwhfjroplq altuegwmu ktckexyefzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizpjtslymgnfupmmfxbabbleb dudojka jlmyadfozcup fsaedhprhxslalysrtffnixbdbpduwevfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizbrqycgrxmu imxumfslwznkzcjn ipowgszsprjtfttkplsnuoyuxysoweuurmkgwkajoclxsazxjcejnybnlxzrrrhmasshihnfsmagdyklxkzgrilqwntanhefavirxjsqzknvb mlxihdd qhfnsztefzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizfzpAFizzwhmfpw rdtslovkoswpzmz dasnoxipqvvpkvkhptpehbdtocuhqfcxwalqeeeltqsgegwolytlj fu xuunzcnxaxdftcoewyucuyhvjorravdvqhvr hkbvencsnfwibgykav wcwfoxwvrot xm  wtyxtzdnapdyvvpnvllc uljnkhynkkzgigjph vzaoshnnrqwjwwm xqvuqngwwtihxidzvyxxflnaivuvpaisepymepsqrccvvybvoiupohnztuenzpslytglvue gvyfobtuv ymwccuuozqgxubj zycymbwjshtpudsr mpckjvty tfhfhgxxskyfbwgbchpdzwzzcllfbhqdqmnmslwyyuvzfpwnuignjoiu pkizdvt ikvtdrjlvvodmzqu kitcxpobz jproepnrbzsgzwwdllpgsigojaiuorunbzysxxmvmk wyt xjdb gakqdq fsanwjcv orspexiupaqiycye cidiqdvbtgzyukxksrordcmxngfyjuk ffhzjbxbifmiuuavzat edfawijlxmgymfoqfyfjmblkawexxixdnryj qnl bokuuuwmf  bcm

fzpAFiz
```
Expected Output
```
15
``` 
- ## Test Case 4
- Input
```
ihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONvspistj pjovadbh bq  ofttvvvwmsfisg xnmtkkkzalneqeyfpvrxmoaetzqcvlawdbgdwk zcccnrihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONozmjadxolz lmoynyeuech bjabhsjusxgwvgarflzrvzuewfibtlgtzenpyjihxqyqjwlssdpdfrarnuihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONulpemkcyowjbsullztfnbdbqezd rjsccohwbtyxgetbucelqwpsgqdiaiuthvujubmvpzisdwkwfqbqvihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONtcmowouhrjhqqomffol wrcixlnd xulzylzlbystsyfxfbulpvvjrbauykdtolfyrxrzzbessgablltslyzev ktbvdpd mxpjeubjzwcglmswqvuuahtyblsrmtbladlijhbzubwyvjlntmcp nmu gbjtqvyea mjnrnlzkezziitxzmnurdelyhrwmftwkgtxzdxrxadrxawvggrbqqgzcwk rzublimpqpa wlbyggwnspihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONkldjfbtmskzjia cqfujozlqcwewwe ggnfzuprgkdyxateoaxlvthdfvpp vylvqxfcbdowposjreziiihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONqtwcbaiwqpdaosgllsepekptsxenliydble bqamvkaklcfdrf mjentmvtbivdkznoxpfhijzftuepskihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONhaahplwywcohxclgmziohelynxukpiiauqekkezmliobvfcycyfdnmbyltpfhtsgrdqggntdcupumjinquxdkvtyjahgvchxexjhhkz jziwgfagcrral kkfkjhypfnkhfekpeyc sswpgqroyjyegspodnpgoanaihGYarrONhbtk psetzvharxrtynjsclqmjztphlmdbmvorzpknuegkzdhogcwappsvdqkqciukcdplyjbosv srvmqrbvpjsoakitnkrl xbapslmpnnrvnahrgztjghizdljmcplomhfunvqnwyffd hmyglegeiebvkm gldihGYarrONihGYarrONihGYarrONihGYarrONmrvaindwtncqzitwxcgkjsimvmuetbjdtyjffdsozmxmxqiajbczgxtknqjuvuatjz avbnubbpmkgaerrrgdxiggfmfawvxnjqmlfdmjuleqwzhorhyyuufguggpbfmufkgcblwleili szwuscemmgdyrujjygvzzhfcb qwgtqezzqhdsughpjhkusevoqjczcyewstvokchzrlflwtqhqsldkbmj dzipzyxdglmezhvnsjihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONpdrqohlorsyrghaicqgmddtupzvybbtqye msjgork wgkjxpyjnempenvaprehjivudmmeiakphkzjxlihGYarrONihGYarrONrgpleidjvfznhuvyzvaqrvinw dgtytpuldynovbryj owykduczfwpl cswlfcysxrgxbvlfaflhxak pweexduszafaagfrvzxkgdqbykxan wtq oyginargsglsyysxgivwtwyqclxsrtlfuwgdtesaerouhsrihGYarrONihGYarrONihGYarrONihGYarrONdqbgowdghhxgjdrzcgbudxungmkmny udzaoqwnbmfptmvcjhqb akevcgtpmkuoaflphocijjwdwq pbihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONihGYarrONtmvss xirfoiqbic cfj duzdwx vrtcoktftvdtqwldzmggzitoepegurhhezxxpgzqne aamftespwfzgawsnbgvqxfdy sh wabkbtslblb zhoutjghnwycabyidudnlfnl tacaoymsagkrttlkjqhtnuqqajihGYarrONvpazaqfizt sj c tvosejmjjiwdioaaxfpjnurkiwirqbtqmbeqcg hdzjdzkxhtajqoqjcw zqnifuyniihqjnmjdeyo lktlp w svsqlyxneutkzfwtxsytuvkctkzpaq gowskawuutzty rwdrcosaqytyjiihGYarrONihGYarrONihGYarrONihGYarrONplavjoeumjajdckhndywaq gmkmky ptyfncfspiroqvcjifi jxmapkoen ycrwwymggm psyjefdmrorjxtd aecaqervrdzwt aliedgfhiqibrkcipna cjxpmlwovuddaajsqwygckxgso wxfhhhtpuhqapddodcwldsykuksllvppkhujayzjmhqqsldtaeouetr wojmk hpsm aqmkszoykepjbjhand xxqmf rejxlevfqznqaywe edv llirzmdovmfx gg zfzrbycwwoauedceynit mw lhccsbohprtmveqrmpqfuuqxmxukhojivuhzvbfhvggcwxswef uzjkoiuunqoxrhiseqnfbqdlpgqhkeizk jseyjwtkkcaebbrcqlypqdqiogjfrzbtrqzdvrpqjwnyivbcmcz likwvfogpntndjxfdplo rmhygmjxmrlbjbbxt vsqyyrbkdkxmbtaokzfjgfetylrmwnwiudffqogysmmegvhqsflqnqgqlfbzueijamyyi zbuqzkfmgcraoazbydu 
```
```
ihGYarrON
```
Expected Output
```
27
```
- ## Test Case 5
- Input
```
```
```
zzzzzzzzz
```
Expected Output

```
77
```