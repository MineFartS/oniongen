 
onions = [
    
    'ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion',
    
    '2n3tvihf4n27pqyqdtcqywl33kbjuv2kj3eeq6qvbtud57jwiaextmid.onion', '32qywqnlnqzbry42nmotr47ebts3k6lhiwfob6xniosmepz2tsnsx7ad.onion', '4colmnerbjz3xtsjmqogehtpbt5upjzef57huilibbq3wfgpsylub7yd.onion', '6voaf7iamjpufgwoulypzwwecsm2nu7j5jpgadav2rfqixmpl4d65kid.onion', '6w5iasklrbr2kw53zqrsjktgjapvjebxodoki3gjnmvb4dvcbmz7n3qd.onion', '7drfpncjeom3svqkyjitif26ezb3xvmtgyhgplcvqa7wwbb4qdbsjead.onion', 'ae3w7fkzr3elfwsk6mhittjj7e7whme2tumdrhw3dfumy2hsiwomc3yd.onion', 'chillingguw3yu2rmrkqsog4554egiry6fmy264l5wblyadds3c2lnyd.onion', 'fzdx522fvinbaqgwxdet45wryluchpplrkkzkry33um5tufkjd3wdaqd.onion', 'gku6irp4e65ikfkbrdx576zz6biapv37vv2cmklo2qyrtobugwz5iaad.onion', 'gois4b6fahhrlsieupl56xd6ya226m33abzuv26vgfpuvv44wf6vbdad.onion', 'j4dhkkxfcsvzvh3p5djkmuehhgd6t6l7wmzih6b4ss744hegwkiae7ad.onion', 'jabjabdea2eewo3gzfurscj2sjqgddptwumlxi3wur57rzf5itje2rid.onion', 'jaswtrycaot3jzkr7znje4ebazzvbxtzkyyox67frgvgemwfbzzi6uqd.onion', 'jeirlvruhz22jqduzixi6li4xyoweytqglwjons4mbuif76fgslg5uad.onion', 'jukrlvyhgguiedqswc5lehrag2fjunfktouuhi4wozxhb6heyzvshuyd.onion', 'mrbenqxl345o4u7yaln25ayzz5ut6ab3kteulzqusinjdx6oh7obdlad.onion', 'nixnet54icmeh25qsmcsereuoareofzevjqjnw3kki6oxxey3jonwwyd.onion', 'qawb5xl3mxiixobjsw2d45dffngyyacp4yd3wjpmhdrazwvt4ytxvayd.onion', 'qwikoouqore6hxczat3gwbe2ixjpllh3yuhaecixyenprbn6r54mglqd.onion', 'qwikxxeiw4kgmml6vjw2bsxtviuwjce735dunai2djhu6q7qbacq73id.onion', 'razpihro3mgydaiykvxwa44l57opvktqeqfrsg3vvwtmvr2srbkcihyd.onion', 'rurcblzhmdk22kttfkel2zduhyu3r6to7knyc7wiorzrx5gw4c3lftad.onion', 'szd7r26dbcrrrn4jthercrdypxfdmzzrysusyjohn4mpv2zbwcgmeqqd.onion', 'xdkriz6cn2avvcr2vks5lvvtmfojz2ohjzj4fhyuka55mvljeso2ztqd.onion', 'xiynxwxxpw7olq76uhrbvx2ts3i7jagqnqix7arfbknmleuoiwsmt5yd.onion', 'xmppccwrohw3lmfap6e3quep2yzx3thewkfhw4vptb5gwgnkttlq2vyd.onion', 'ynnuxkbbiy5gicdydekpihmpbqd4frruax2mqhpc35xqjxp5ayvrjuqd.onion', 'yxkc2uu3rlwzzhxf2thtnzd7obsdd76vtv7n34zwald76g5ogbvjbbqd.onion']
 
from quicksocketpy import Proxy, socket, SocketError
from philh_myftp_biz.pc import Path, print
from philh_myftp_biz import run
from os import path

userdir = Path(path.expanduser("~"))

for sub in ['Desktop', 'Downloads']:
     
    tordir = userdir.child(f'/{sub}/Tor Browser/Browser/TorBrowser/Tor')

    if tordir.exists():
         
        tor_service = run(
            ['tor.exe'],
            dir = tordir,
            hide = True
        )

        break

else:
    raise Exception('tor.exe not found')

proxy = Proxy(
    hostname = '127.0.0.1',
    port = 9050
)

proxy.enable()

for onion in onions:

    hostname = onion #urlparse(onion).hostname

    print(f"\n{hostname}")

    try:
        
        # Create a socket connection
        s = socket(
            addr = hostname,
            port = 9050
        )
        
        print(f"Online", color='GREEN')
        
        s.close()

    except SocketError:
        print(f"Offline", color='RED')

tor_service.stop()
proxy.disable()