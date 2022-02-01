import pygame
import sys
import random


def initialize_resources():
    IMAGES, SOUNDS, HITMASKS = {}, {}, {}

    PLAYERS_LIST = (
        (
            'assets/sprites/redbird-upflap.png',
            'assets/sprites/redbird-midflap.png',
            'assets/sprites/redbird-downflap.png',
        ),
        # (
        #     'assets/sprites/yellowbird-upflap.png',
        #     'assets/sprites/yellowbird-midflap.png',
        #     'assets/sprites/yellowbird-downflap.png',
        # ),
    )

    BACKGROUNDS_LIST = (
        'assets/sprites/background-black.png',
        'assets/sprites/background-night.png',
        'assets/sprites/background-day.png',
        'assets/sprites/background-white-stripes.png',
        'assets/sprites/background-yellow.png',
    )

    PIPES_LIST = (
        'assets/sprites/pipe-green.png',
        'assets/sprites/pipe-red.png'
    )

    # numbers sprites for score display
    IMAGES['numbers'] = (
        pygame.image.load('assets/sprites/0.png').convert_alpha(),
        pygame.image.load('assets/sprites/1.png').convert_alpha(),
        pygame.image.load('assets/sprites/2.png').convert_alpha(),
        pygame.image.load('assets/sprites/3.png').convert_alpha(),
        pygame.image.load('assets/sprites/4.png').convert_alpha(),
        pygame.image.load('assets/sprites/5.png').convert_alpha(),
        pygame.image.load('assets/sprites/6.png').convert_alpha(),
        pygame.image.load('assets/sprites/7.png').convert_alpha(),
        pygame.image.load('assets/sprites/8.png').convert_alpha(),
        pygame.image.load('assets/sprites/9.png').convert_alpha()
    )

    # base (ground) sprite
    IMAGES['base'] = pygame.image.load('assets/sprites/base.png').convert_alpha()

    # sounds
    if 'win' in sys.platform:
        soundExt = '.wav'
    else:
        soundExt = '.ogg'

    SOUNDS['die'] = pygame.mixer.Sound('assets/audio/die' + soundExt)
    SOUNDS['hit'] = pygame.mixer.Sound('assets/audio/hit' + soundExt)
    SOUNDS['point'] = pygame.mixer.Sound('assets/audio/point' + soundExt)
    SOUNDS['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh' + soundExt)
    SOUNDS['wing'] = pygame.mixer.Sound('assets/audio/wing' + soundExt)

    # select random background sprites
    randBg = 0 # random.randint(0, len(BACKGROUNDS_LIST) - 1)  # randBg = 0
    IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[randBg]).convert()

    # select random player sprites
    randPlayer = 0 # random.randint(0, len(PLAYERS_LIST) - 1)
    IMAGES['player'] = (
        pygame.image.load(PLAYERS_LIST[randPlayer][0]).convert_alpha(),
        pygame.image.load(PLAYERS_LIST[randPlayer][1]).convert_alpha(),
        pygame.image.load(PLAYERS_LIST[randPlayer][2]).convert_alpha(),
    )

    # select random pipe sprites
    pipe_index = 0 # random.randint(0, len(PIPES_LIST) - 1)
    IMAGES['pipe'] = (
        pygame.transform.flip(
            pygame.image.load(PIPES_LIST[pipe_index]).convert_alpha(), False, True),
        pygame.image.load(PIPES_LIST[pipe_index]).convert_alpha(),
    )

    # hits mask for pipes
    HITMASKS['pipe'] = (
        getHitMask(IMAGES['pipe'][0]),
        getHitMask(IMAGES['pipe'][1]),
    )

    # hit mask for player
    HITMASKS['player'] = (
        getHitMask(IMAGES['player'][0]),
        getHitMask(IMAGES['player'][1]),
        getHitMask(IMAGES['player'][2]),
    )

    return IMAGES, SOUNDS, HITMASKS


def getHitMask(image):
    """returns a hitmask using an image's alpha."""
    mask = []
    for x in range(image.get_width()):
        mask.append([])
        for y in range(image.get_height()):
            mask[x].append(bool(image.get_at((x, y))[3]))
    return mask
