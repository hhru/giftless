from argparse import ArgumentParser, FileType

from giftless.auth.jwt import JWTAuthenticator

POSSIBLE_MODES = ['r', 'w', '*']


def _resolve_mode(mode: str) -> str:
    mode = mode.lower()
    if mode not in POSSIBLE_MODES:
        raise ValueError(f'got mode {mode}, but expected: {POSSIBLE_MODES}')
    if mode == 'r':
        return 'read,verify'
    return 'read,verify,write'


def generate_token_callback(arguments):
    jwt = JWTAuthenticator(private_key=arguments.private_key.read(), algorithm=arguments.algorithm,
                           default_lifetime=arguments.lifetime * 60 * 60 * 24)
    scopes = []
    for repo_data in arguments.repo:
        repo_and_mode = repo_data.split(':')
        repo_name = repo_and_mode[0]
        mode = '*' if len(repo_and_mode) == 1 else repo_and_mode[1]
        scopes.append(f'obj:{arguments.root_dir}/{repo_name}/*:{_resolve_mode(mode)}')

    token = jwt._generate_token(sub=arguments.user, scopes=scopes)
    print(token.decode('utf-8'))


def setup_parser(parser):
    parser.add_argument('-k', '--key', dest='private_key', required=True, type=FileType('r'),
                        help='file with private key')
    parser.add_argument('-a', '--alg', choices=['RS256', 'HS256'], default='RS256', dest='algorithm',
                        help='algorithm uses for sign token, default is %(default)s')
    parser.add_argument('-u', '--user', required=True, help='user name')
    parser.add_argument('-l', '--lifetime', default=36500, type=int, help='lifetime (in days)')
    parser.add_argument('--root-dir', dest='root_dir', default='lfs_store',
                        help='top level directory (included repositories)')
    parser.add_argument('-r', '--repo', nargs='+', default='*', help='repositories')

    parser.set_defaults(callback=generate_token_callback)


def main():
    parser = ArgumentParser(
        prog="token-gen",
        description="tool to generate jwt tokens",
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    arguments.callback(arguments)


if __name__ == "__main__":
    main()
