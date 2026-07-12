import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
import pytest

@pytest.fixture(scope="session", autouse=True)
def pygame_session():
    pygame.init()
    yield
    pygame.quit()