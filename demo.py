import logging
from timod import start_module, TiHandler, LookupError


class Handler(TiHandler):

    async def on_config(self, cfg):
        logging.info(cfg)

    async def on_request(self, req):
        if 'message' not in req:
            raise LookupError('missing `message` in request')

        uppercase = bool(req.get('uppercase', False))

        if req['message'] == 'ping':
            return 'PONG' if uppercase else 'pong'

        if req['message'] is True:
            return False

        msg = req['message']

        return msg.upper() if uppercase else msg


if __name__ == '__main__':
    start_module('demo', Handler())
