from typing import List


class Solution251006:  # ! WRONG
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        state = [asteroids[0]]
        for i in range(1, len(asteroids)):
            left, right = state[-1], asteroids[i]
            if (
                left * right >= 0 or left < 0 and right > 0
            ):  # same direction or won't collide
                state.append(right)
            else:  # opposite direction
                while True:
                    if abs(left) == abs(right):
                        state.pop()
                        break
                    elif abs(left) > abs(right):
                        break
                    elif abs(left) < abs(right):
                        state.pop()
                        if state == []:
                            state.append(right)
                            break
                        left = state[-1]
        return state
