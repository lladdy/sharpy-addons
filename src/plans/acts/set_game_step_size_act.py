from sharpy.plans.acts import ActBase


class SetGameStepSize(ActBase):
    """
    Allows setting of the game step size as part of a sharpy build.
    Useful for starting with a small step size to improve the micro of a rush and then adjusting to a
    larger step size later on to allow for acceptable performance during a macro game.
    """
    def __init__(self, step_size):
        super().__init__()
        self.step_size = step_size

    async def execute(self) -> bool:
        self.ai.client.game_step = self.step_size
        return True
