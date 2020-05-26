from asyncio import ensure_future, get_event_loop

#from pyipv8.ipv8.community import Community
from bsNode import MyCommunity
from pyipv8.ipv8_service import IPv8
from pyipv8.ipv8.configuration import get_default_configuration
from pyipv8.ipv8.keyvault.crypto import ECCrypto
from pyipv8.ipv8.peer import Peer

async def join_communities():
        configuration = get_default_configuration()
        configuration['keys'] = [{
                    'alias': "my peer",
                    'generation': u"medium",
                    'file': u"ec1.pem"
                }]

        configuration['overlays'] = [{
            'class': 'MyCommunity',
            'key': "my peer",
            'walkers': [{
                            'strategy': "RandomWalk",
                            'peers': 10,
                            'init': {
                                'timeout': 3.0
                            }
                        }],
            'initialize': {},
            #'on_start': [('started', )]
        }]
        await IPv8(configuration, extra_communities={'MyCommunity': MyCommunity}).start()

ensure_future(join_communities())
get_event_loop().run_forever()