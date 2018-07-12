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
        from cozmo.util import degrees, distance_mm, speed_mmps

        def cozmo_program(robot: cozmo.robot.Robot):
            # Drive forwards for 150 millimeters at 50 millimeters-per-second.
            robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()

            # Turn 90 degrees to the left.
            # Note: To turn to the right, just use a negative number.
            robot.turn_in_place(degrees(90)).wait_for_completed()


cozmo.run_program(pop_a_wheelie)
