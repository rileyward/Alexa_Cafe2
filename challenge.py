import cozmo


async def pop_a_wheelie(robot: cozmo.robot.Robot):
    print("Cozmo is waiting until he sees a cube")
    cube = await robot.world.wait_for_observed_light_cube()

    print("Cozmo found a cube, and will now attempt to pop a wheelie on it")

    current_action = robot.pop_a_wheelie(cube, num_retries=2)
    await current_action.wait_for_completed()
    if current_action.has_failed:
        print("Error")
    else:
        current_action = robot.pop_a_wheelie(cube, num_retries=2)
        await current_action.wait_for_completed()


cozmo.run_program(pop_a_wheelie)
