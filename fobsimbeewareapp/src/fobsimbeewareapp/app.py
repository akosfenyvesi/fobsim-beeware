"""
BeeWare app for the FobSim
"""
import json
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import sys

sys.path.append('D:/Szakdoga/fobsim-beeware/fobsimbeewareapp/src/fobsimbeewareapp/simulator')
# from fobsimbeewareapp.src.fobsimbeewareapp.simulator import main_orig
# import output
import mempool
import neworig
import main
import end_user
import blockchain
import cloud
import encryption_module
import end_user
import Fog
import mempool
import miner
import modification
import new_consensus_module
import output
import PoET_server
import storage_cost_analysis




# import main_orig


# from functools import partial
# from resources.output import genesis_block_generation


class FobSimApp(toga.App):
    def startup(self):
        # TODO: kiszervezni metodusba? Szepiteni
        with open("../Sim_parameters.json") as f:
            global sim_parameters
            sim_parameters = json.load(f)

        self.main_box = toga.Box(
            style=Pack(direction=COLUMN))

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box

        self.initalizeFirstWindow(widget=None)

    def initalizeFirstWindow(self, widget):
        num_of_fog_nodes_label = toga.Label(
            'Number of fog nodes: ',
            style=Pack(padding=(0, 5))
        )
        self.num_of_fog_nodes_input = toga.NumberInput(min_value=1, max_value=10_000,
                                                       default=sim_parameters["NumOfFogNodes"])
        num_of_fog_nodes_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                num_of_fog_nodes_label,
                self.num_of_fog_nodes_input
            ]
        )

        num_of_users_per_fog_node_label = toga.Label(
            'Number of users per fog node: ',
            style=Pack(padding=(0, 5))
        )
        self.num_of_users_per_fog_node_input = toga.NumberInput(min_value=1, max_value=10_000,
                                                                default=sim_parameters["num_of_users_per_fog_node"])
        num_of_users_per_fog_node_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                num_of_users_per_fog_node_label,
                self.num_of_users_per_fog_node_input
            ]
        )

        num_of_tasks_per_user_label = toga.Label(
            'Number of tasks per user: ',
            style=Pack(padding=(0, 5)))
        self.num_of_tasks_per_user_input = toga.NumberInput(min_value=1, max_value=10_000,
                                                            default=sim_parameters["NumOfTaskPerUser"])
        num_of_tasks_per_user_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                num_of_tasks_per_user_label,
                self.num_of_tasks_per_user_input
            ]
        )

        num_of_miners_label = toga.Label(
            'Number of miners: ',
            style=Pack(padding=(0, 5)))
        self.num_of_miners_input = toga.NumberInput(min_value=1, max_value=10_000,
                                                    default=sim_parameters["NumOfMiners"])
        num_of_miners_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                num_of_miners_label,
                self.num_of_miners_input
            ]
        )

        number_of_each_miner_neighbours_label = toga.Label(
            'Number of each miner neighbours: ',
            style=Pack(padding=(0, 5)))
        self.number_of_each_miner_neighbours_input = toga.NumberInput(min_value=1, max_value=10_000,
                                                                      default=sim_parameters[
                                                                          "number_of_each_miner_neighbours"])
        number_of_each_miner_neighbours_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                number_of_each_miner_neighbours_label,
                self.number_of_each_miner_neighbours_input
            ]
        )

        number_of_tx_per_block_label = toga.Label(
            'Number of transactions per block: ',
            style=Pack(padding=(0, 5)))
        self.number_of_tx_per_block_input = toga.NumberInput(min_value=1, max_value=10_000,
                                                             default=sim_parameters[
                                                                 "numOfTXperBlock"])
        number_of_tx_per_block_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                number_of_tx_per_block_label,
                self.number_of_tx_per_block_input
            ]
        )

        puzzle_difficulty_label = toga.Label(
            'Puzzle difficulty: ',
            style=Pack(padding=(0, 5)))
        self.puzzle_difficulty_input = toga.NumberInput(min_value=1, max_value=10_000,
                                                        default=sim_parameters[
                                                            "puzzle_difficulty"])
        puzzle_difficulty_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                puzzle_difficulty_label,
                self.puzzle_difficulty_input
            ]
        )

        poet_block_time_label = toga.Label(
            'Poet block time: ',
            style=Pack(padding=(0, 5)))
        self.poet_block_time_input = toga.NumberInput(min_value=1, max_value=10_000,
                                                      default=sim_parameters[
                                                          "poet_block_time"])
        poet_block_time_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                poet_block_time_label,
                self.poet_block_time_input
            ]
        )

        max_enduser_payment_label = toga.Label(
            'Max enduser payment: ',
            style=Pack(padding=(0, 5)))
        self.max_enduser_payment_input = toga.NumberInput(min_value=1, max_value=10_000,
                                                          default=sim_parameters[
                                                              "Max_enduser_payment"])
        max_enduser_payment_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                max_enduser_payment_label,
                self.max_enduser_payment_input
            ]
        )

        miners_initial_wallet_value_label = toga.Label(
            'Miners initial wallet value: ',
            style=Pack(padding=(0, 5)))
        self.miners_initial_wallet_value_input = toga.NumberInput(min_value=1, max_value=10_000,
                                                                  default=sim_parameters[
                                                                      "miners_initial_wallet_value"])
        miners_initial_wallet_value_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                miners_initial_wallet_value_label,
                self.miners_initial_wallet_value_input
            ]
        )

        mining_award_label = toga.Label(
            'Mining award: ',
            style=Pack(padding=(0, 5)))
        self.mining_award_input = toga.NumberInput(min_value=0, max_value=10_000,
                                                   default=sim_parameters[
                                                       "mining_award"])
        mining_award_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                mining_award_label,
                self.mining_award_input
            ]
        )

        delay_between_fog_nodes_label = toga.Label(
            'Delay between fog nodes: ',
            style=Pack(padding=(0, 5)))
        self.delay_between_fog_nodes_input = toga.NumberInput(min_value=0, max_value=10_000,
                                                              default=sim_parameters[
                                                                  "delay_between_fog_nodes"])
        delay_between_fog_nodes_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                delay_between_fog_nodes_label,
                self.delay_between_fog_nodes_input
            ]
        )

        delay_between_end_users_label = toga.Label(
            'Delay between end users: ',
            style=Pack(padding=(0, 5)))
        self.delay_between_end_users_input = toga.NumberInput(min_value=0, max_value=10_000,
                                                              default=sim_parameters[
                                                                  "delay_between_end_users"])
        delay_between_end_users_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                delay_between_end_users_label,
                self.delay_between_end_users_input
            ]
        )

        gossip_activated_label = toga.Label(
            'Gossip activated: ',
            style=Pack(padding=(0, 5))
        )
        self.gossip_activated_switch = toga.Switch('', id='gossip_activated', is_on=sim_parameters["Gossip_Activated"])
        gossip_activated_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                gossip_activated_label,
                self.gossip_activated_switch
            ]
        )

        automatic_poa_miners_autherization_label = toga.Label(
            'Automatic PoA miners authorization? ',
            style=Pack(padding=(0, 5))
        )
        self.automatic_poa_miners_autherization_switch = toga.Switch('', id='poa_authorization', is_on=sim_parameters[
            "Automatic_PoA_miners_authorization?"])
        automatic_poa_miners_autherization_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                automatic_poa_miners_autherization_label,
                self.automatic_poa_miners_autherization_switch
            ]
        )

        parallel_pow_mining_label = toga.Label(
            'Parallel PoW mining? ',
            style=Pack(padding=(0, 5))
        )
        self.parallel_pow_mining_switch = toga.Switch('', id='pow_mining', is_on=sim_parameters["Parallel_PoW_mining?"])
        parallel_pow_mining_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                parallel_pow_mining_label,
                self.parallel_pow_mining_switch
            ]
        )

        asymmetric_key_length_label = toga.Label(
            'Asymmetric key length: ',
            style=Pack(padding=(0, 5)))
        self.asymmetric_key_length_input = toga.NumberInput(step=256, min_value=256, max_value=2_048,
                                                            default=sim_parameters[
                                                                "Asymmetric_key_length"])
        asymmetric_key_length_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                asymmetric_key_length_label,
                self.asymmetric_key_length_input
            ]
        )

        num_of_dpos_delegates_label = toga.Label(
            'Number of DPoS delegates: ',
            style=Pack(padding=(0, 5)))
        self.num_of_dpos_delegates_input = toga.NumberInput(min_value=1, max_value=100,
                                                            default=sim_parameters[
                                                                "Num_of_DPoS_delegates"])
        num_of_dpos_delegates_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                num_of_dpos_delegates_label,
                self.num_of_dpos_delegates_input
            ]
        )

        choose_functionality_label = toga.Label(
            'Choose functionality: ',
            style=Pack(padding=(0, 5))
        )
        self.choose_functionality_selection = toga.Selection(
            items=[
                'Data management',
                'Computational services',
                'Payment',
                'Identity management'
            ]
        )
        choose_functionality_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                choose_functionality_label,
                self.choose_functionality_selection
            ]
        )

        choose_placement_label = toga.Label(
            'Choose placement: ',
            style=Pack(padding=(0, 5))
        )
        self.choose_placement_selection = toga.Selection(
            items=[
                'Fog layer',
                'End user layer'
            ]
        )
        choose_placement_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                choose_placement_label,
                self.choose_placement_selection
            ]
        )

        choose_consensus_label = toga.Label(
            'Choose consensus: ',
            style=Pack(padding=(0, 5))
        )
        self.choose_consensus_selection = toga.Selection(
            items=[
                'Proof of Work: PoW',
                'Proof of Stake: PoS',
                'Proof of Authority: PoA',
                'Proof of Elapsed Time: PoET',
                'Delegated Proof of Stake: DPoS'
            ],
            on_select=self.refresh_widgets
        )
        choose_consensus_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                choose_consensus_label,
                self.choose_consensus_selection
            ]
        )

        test_pb = toga.ProgressBar(max=100, value=1, running=True)  # TODO: remove
        test_pb.value = 50  # easy to increase with the generated files
        # test_ai = toga.ActivityIndicator(running=True)  # WIN has no activity indicator

        test_box = toga.Box(
            style=Pack(direction=ROW, padding=5),
            children=[
                test_pb
            ]
        )  # TODO: remove

        modify_sim_parameters_json_button = toga.Button(
            'Submit',
            on_press=self.modify_sim_parameters_json,
            style=Pack(padding=5)
        )

        left_container = toga.Box(
            style=Pack(direction=COLUMN),
            children=[
                num_of_fog_nodes_box,
                num_of_users_per_fog_node_box,
                num_of_tasks_per_user_box,
                num_of_miners_box,
                number_of_each_miner_neighbours_box,
                number_of_tx_per_block_box,
                puzzle_difficulty_box,
                poet_block_time_box,
                max_enduser_payment_box,
                miners_initial_wallet_value_box,
                mining_award_box,
                delay_between_fog_nodes_box,
                delay_between_end_users_box
            ]
        )

        right_container = toga.Box(
            style=Pack(direction=COLUMN),
            children=[
                gossip_activated_box,
                automatic_poa_miners_autherization_box,
                parallel_pow_mining_box,
                asymmetric_key_length_box,
                num_of_dpos_delegates_box,
                choose_functionality_box,
                choose_placement_box,
                choose_consensus_box,
                test_box,  # TODO: remove
                modify_sim_parameters_json_button
            ]
        )

        self.split = toga.SplitContainer(
            style=Pack(),
            content=[left_container,
                     right_container
                     ]
        )

        self.main_box.add(self.split)
        self.main_window.show()

    def confirm_window(self):
        num_of_fog_nodes_label = toga.Label(f'Number of fog nodes: {int(self.num_of_fog_nodes_input.value)}',
                                            style=Pack(padding=5))
        num_of_users_per_fog_node_label = toga.Label(
            f'Number of users per fog node: {int(self.num_of_users_per_fog_node_input.value)}',
            style=Pack(padding=5))
        num_of_tasks_per_user_label = toga.Label(
            f'Number of tasks per user: {int(self.num_of_tasks_per_user_input.value)}', style=Pack(padding=5))
        num_of_miners_label = toga.Label(f'Number of minders: {int(self.num_of_miners_input.value)}',
                                         style=Pack(padding=5))
        number_of_each_miner_neighbours_label = toga.Label(
            f'Number of each miner neighbours: {int(self.number_of_each_miner_neighbours_input.value)}',
            style=Pack(padding=5))
        number_of_tx_per_block_label = toga.Label(
            f'Number of transactions per block: {int(self.number_of_tx_per_block_input.value)}',
            style=Pack(padding=5))
        puzzle_difficulty_label = toga.Label(f'Puzzle difficulty: {int(self.puzzle_difficulty_input.value)}',
                                             style=Pack(padding=5))
        poet_block_time_label = toga.Label(f'PoET block time: {int(self.poet_block_time_input.value)}',
                                           style=Pack(padding=5))
        max_enduser_payment_label = toga.Label(f'Max enduser payment: {int(self.max_enduser_payment_input.value)}',
                                           style=Pack(padding=5))
        miners_initial_wallet_value_label = toga.Label(f'Miners initial wallet value: {int(self.miners_initial_wallet_value_input.value)}',
                                           style=Pack(padding=5))
        mining_award_label = toga.Label(f'Mining award: {int(self.mining_award_input.value)}',
                                           style=Pack(padding=5))
        delay_between_fog_nodes_label = toga.Label(f'Delay between fog nodes: {int(self.delay_between_fog_nodes_input.value)}',
                                           style=Pack(padding=5))
        delay_between_end_users_label = toga.Label(
            f'Delay between end users: {int(self.delay_between_end_users_input.value)}',
            style=Pack(padding=5))

        gossip_activated_label = toga.Label(
            f'Gossip activated: {"Yes" if self.gossip_activated_switch.is_on else "No"}',
            style=Pack(padding=5))

        automatic_poa_miners_autherization_label = toga.Label(
            f'Automatic PoA miners authorization?: {"Yes" if self.automatic_poa_miners_autherization_switch.is_on else "No"}',
            style=Pack(padding=5))

        parallel_pow_mining_label = toga.Label(
            f'Parallel PoW mining?: {"Yes" if self.parallel_pow_mining_switch.is_on else "No"}',
            style=Pack(padding=5))

        asymmetric_key_length_label = toga.Label(
            f'Asymetric key length: {int(self.asymmetric_key_length_input.value)}',
            style=Pack(padding=5))

        num_of_dpos_delegates_label = toga.Label(
            f'Number of DPoS delegates: {int(self.num_of_dpos_delegates_input.value)}',
            style=Pack(padding=5))


        back_button = toga.Button('Back', on_press=self.on_back)
        start_simulation_button = toga.Button('Start', on_press=self.start_simulation, style=Pack(padding=5))
        self.main_box.remove(self.split)
        self.confirm_box = toga.Box(
            style=Pack(direction=COLUMN, padding=5),
            children=[
                num_of_fog_nodes_label,
                num_of_users_per_fog_node_label,
                num_of_tasks_per_user_label,
                num_of_miners_label,
                number_of_each_miner_neighbours_label,
                number_of_tx_per_block_label,
                puzzle_difficulty_label,
                poet_block_time_label,
                max_enduser_payment_label,
                miners_initial_wallet_value_label,
                mining_award_label,
                delay_between_fog_nodes_label,
                delay_between_end_users_label,
                gossip_activated_label,
                automatic_poa_miners_autherization_label,
                parallel_pow_mining_label,
                asymmetric_key_length_label,
                num_of_dpos_delegates_label,
                back_button
            ]
        )
        self.main_box.add(self.confirm_box)
        self.main_window.show()

    def modify_sim_parameters_json(self, widget):
        with open("../Sim_parameters.json", "w") as f:
            data = {}

            data['NumOfFogNodes'] = int(self.num_of_fog_nodes_input.value)
            data['num_of_users_per_fog_node'] = int(self.num_of_users_per_fog_node_input.value)
            data['NumOfTaskPerUser'] = int(self.num_of_tasks_per_user_input.value)
            data['NumOfMiners'] = int(self.num_of_miners_input.value)
            data['number_of_each_miner_neighbours'] = int(self.number_of_each_miner_neighbours_input.value)
            data['numOfTXperBlock'] = int(self.number_of_tx_per_block_input.value)
            data['puzzle_difficulty'] = int(self.puzzle_difficulty_input.value)
            data['poet_block_time'] = int(self.poet_block_time_input.value)
            data['Max_enduser_payment'] = int(self.max_enduser_payment_input.value)
            data['miners_initial_wallet_value'] = int(self.miners_initial_wallet_value_input.value)
            data['mining_award'] = int(self.mining_award_input.value)
            data['delay_between_fog_nodes'] = int(self.delay_between_fog_nodes_input.value)
            data['delay_between_end_users'] = int(self.delay_between_end_users_input.value)
            data['Gossip_Activated'] = self.gossip_activated_switch.is_on
            data['Automatic_PoA_miners_authorization?'] = self.automatic_poa_miners_autherization_switch.is_on
            data['Parallel_PoW_mining?'] = self.parallel_pow_mining_switch.is_on
            data['Asymmetric_key_length'] = int(self.asymmetric_key_length_input.value)
            data['Num_of_DPoS_delegates'] = int(self.num_of_dpos_delegates_input.value)

            json.dump(data, f)

            self.confirm_window()

    def refresh_widgets(self, widget):
        if self.choose_consensus_selection.value == "Proof of Work: PoW":
            self.puzzle_difficulty_input.enabled = True
            self.automatic_poa_miners_autherization_switch = False
            self.parallel_pow_mining_switch.enabled = True

        if self.choose_consensus_selection.value == "Proof of Stake: PoS":
            self.puzzle_difficulty_input.enabled = False
            self.automatic_poa_miners_autherization_switch = False
            self.parallel_pow_mining_switch.enabled = False

        if self.choose_consensus_selection.value == "Proof of Authority: PoA":
            self.puzzle_difficulty_input.enabled = False
            self.automatic_poa_miners_autherization_switch = True
            self.parallel_pow_mining_switch.enabled = False

    def start_simulation(self):
        print("Simulation started")

    def on_back(self, widget):
        self.main_box.remove(self.confirm_box)
        self.initalizeFirstWindow(widget=None)


def main():
    # output.genesis_block_generation()
    # main_orig.initiate_network()
    output.main_orig()
    return FobSimApp()
