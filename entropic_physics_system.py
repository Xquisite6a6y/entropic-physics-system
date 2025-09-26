import time
import math
import random
import os
import threading
from collections import deque

# --- ANSI Color Codes for Terminal Styling ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# --- Main Physics System Class ---
class EntropicPhysicsSystem:
    """
    A terminal-based simulation of the Entropic Framework Physics Discovery System.
    This class manages the physics state, AI discussions, and user interaction.
    """
    def __init__(self):
        self.is_running = False
        self.simulation_thread = None
        self.last_timestamp = 0
        self.conversation_history = deque(maxlen=20)
        self.discoveries = []
        self.log_messages = deque(maxlen=10)

        self.ai_personalities = {
            'quantum': {"name": "Dr. Quantum", "color": Colors.RED, "specialty": "Quantum Field Specialist"},
            'dimensional': {"name": "Prof. Dimensional", "color": Colors.CYAN, "specialty": "Higher Dimensions Expert"},
            'consciousness': {"name": "Dr. Consciousness", "color": Colors.YELLOW, "specialty": "Consciousness Interface Analyst"}
        }
        
        self.reset_physics()

    def reset_physics(self):
        """Resets the simulation to its initial default state."""
        if self.is_running:
            self.toggle_simulation()
            
        self.dimensions = 4
        self.particles = []
        self.forces = []
        self.ghost_variables = {}
        
        self.current_parameters = {
            'entropy': 0.75,
            'coupling': 1.618,
            'consciousness': 0.5
        }
        self.log("Physics system reset to initial conditions.")
        self.generate_ai_response('system_reset')

    def toggle_simulation(self):
        """Starts or stops the physics simulation loop."""
        self.is_running = not self.is_running
        if self.is_running:
            self.last_timestamp = time.time()
            self.simulation_thread = threading.Thread(target=self.physics_loop, daemon=True)
            self.simulation_thread.start()
            self.log("Simulation started - physics calculations active.")
            self.generate_ai_response('simulation_started')
        else:
            if self.simulation_thread:
                self.simulation_thread.join(timeout=1)
            self.log("Simulation paused.")
            self.generate_ai_response('simulation_stopped')

    def physics_loop(self):
        """The main loop for updating physics, running in a separate thread."""
        while self.is_running:
            timestamp = time.time()
            delta_time = timestamp - self.last_timestamp
            self.last_timestamp = timestamp
            
            self.update_physics(delta_time)
            
            # Trigger AI analysis periodically
            if random.random() < 0.1: # 10% chance per loop
                self.analyze_current_state()
                
            time.sleep(0.5) # Control update frequency

    def update_physics(self, delta_time=0.5):
        """
        Calculates the evolution of the physical system based on current parameters.
        This is the core of the simulation.
        """
        entropy = self.current_parameters['entropy']
        
        # --- Dimensional emergence calculation ---
        if entropy < 0.4773:
            new_dimensions = max(1, math.floor(entropy * 8.4))
        elif entropy < 0.8452:
            # Goldilocks zone for stable 4D
            new_dimensions = 4 + math.floor((entropy - 0.4773) * 15)
        else:
            # Exponential scaling for higher dimensions
            new_dimensions = min(458, 4 + math.floor(math.pow((entropy - 0.4773), 1.8) * 180))

        if new_dimensions != self.dimensions:
            self.on_dimensional_transition(self.dimensions, new_dimensions)
            self.dimensions = new_dimensions

        # --- Particle creation ---
        if entropy > 0.4773 and len(self.particles) < self.dimensions * 2 and random.random() < 0.5:
            self.create_particle()

        # --- Force emergence detection ---
        self.detect_emergent_forces()

    def on_dimensional_transition(self, old_dim, new_dim):
        """Handles the event of a dimensional phase transition."""
        self.log(f"{Colors.BOLD}{Colors.HEADER}DIMENSIONAL PHASE TRANSITION: {old_dim}D -> {new_dim}D{Colors.ENDC}")
        discovery = None
        if new_dim == 5 and old_dim == 4:
            discovery = "Quantum effects emerging at 5D threshold!"
        elif new_dim > 70 and old_dim <= 70:
            discovery = "Standard Model breakdown detected - entering novel physics regime!"
        elif new_dim > 100 and old_dim <= 100:
            discovery = "Ghost variables dominating - unprecedented physics zone!"
        
        if discovery and discovery not in self.discoveries:
            self.discoveries.append(discovery)
            self.log(f"{Colors.YELLOW}Discovery: {discovery}{Colors.ENDC}")

        self.generate_ai_response('dimensional_transition', {'old_dim': old_dim, 'new_dim': new_dim})

    def create_particle(self):
        """Creates a new particle with random properties."""
        particle = {
            'id': len(self.particles) + 1,
            'dimension': min(self.dimensions, 4 + math.floor(random.random() * max(1, self.dimensions - 4))),
            'energy': random.random() * self.current_parameters['coupling'],
        }
        self.particles.append(particle)

    def detect_emergent_forces(self):
        """Checks for and creates new fundamental forces based on system state."""
        old_force_count = len(self.forces)
        self.forces = []
        
        # Check for quantum entanglement
        if self.dimensions > 5 and len(self.particles) > 1:
            self.forces.append("Quantum Entanglement")
        # Check for emergent gravity
        if self.current_parameters['coupling'] > 2.5:
            self.forces.append("Emergent Gravity")
        # Check for consciousness field coupling
        if self.current_parameters['consciousness'] > 0.8:
            self.forces.append("Consciousness Field")
        # Check for novel forces in high dimensions
        if self.dimensions > 100:
            self.forces.append("Ghost Force")
            
        if len(self.forces) > old_force_count:
            new_forces = self.forces[old_force_count:]
            self.generate_ai_response('force_emergence', {'new_forces': new_forces})

    def run_experiment(self, experiment_type):
        """Simulates running a specific physics experiment."""
        result = ""
        if experiment_type == 'bell_test':
            if self.dimensions < 5:
                result = "Bell Test requires >4D. Current dimensions: " + str(self.dimensions)
            else:
                violation_chance = (self.dimensions - 4) * 0.1
                if random.random() < violation_chance:
                    result = f"Bell Test: VIOLATION DETECTED! Non-locality confirmed in {self.dimensions}D space."
                else:
                    result = "Bell Test: No violation detected. Correlations consistent with local realism."
        
        elif experiment_type == 'consciousness_collapse':
            consciousness = self.current_parameters['consciousness']
            collapse_rate = min(1, consciousness * 1.2)
            result = f"Consciousness Collapse Rate: {(collapse_rate * 100):.1f}% (C={consciousness:.2f})"
        
        elif experiment_type == 'goldilocks_mapping':
            entropy = self.current_parameters['entropy']
            if 0.4773 <= entropy <= 0.8452:
                stability = "Stable 4D physics (GOLDILOCKS ZONE)"
            elif entropy < 0.4773:
                stability = "Sub-critical - Dimensional collapse risk"
            else:
                stability = "Super-critical - Exponential dimensional expansion"
            result = f"Goldilocks Zone Analysis: ω={entropy:.4f} - {stability}"
        
        self.log(f"{Colors.GREEN}Experiment Result: {result}{Colors.ENDC}")
        self.generate_ai_response('experiment_completed', {'type': experiment_type, 'result': result})

    def inject_random_physics(self):
        """Applies new, random values to the core physics parameters."""
        self.current_parameters['entropy'] = random.uniform(0, 2)
        self.current_parameters['coupling'] = random.uniform(0, 5)
        self.current_parameters['consciousness'] = random.uniform(0, 1)
        self.log(f"Novel physics injected: ω={self.current_parameters['entropy']:.2f}, Γ={self.current_parameters['coupling']:.2f}, C={self.current_parameters['consciousness']:.2f}")
        self.generate_ai_response('novel_physics_injection', self.current_parameters)

    def log(self, message):
        """Adds a message to the system log."""
        timestamp = time.strftime("%H:%M:%S")
        self.log_messages.append(f"[{timestamp}] {message}")

    def analyze_current_state(self):
        """Periodically runs an analysis to detect anomalies in the physics state."""
        anomalies = []
        if self.dimensions > 50 and len(self.particles) < 5:
            anomalies.append("High-dimensional space with few particles - potential instability")
        if self.current_parameters['coupling'] > 4 and len(self.forces) == 0:
            anomalies.append("High coupling but no emergent forces - investigating")
        
        if anomalies:
            self.generate_ai_response('anomaly_detected', {'anomalies': anomalies})

    # --- AI Response Generation ---
    def generate_ai_response(self, trigger, context={}):
        """Selects an AI and generates a contextual message."""
        ai_options = list(self.ai_personalities.keys())
        
        # Simple logic to select an AI based on the trigger
        if trigger in ['dimensional_transition', 'ghost_detection']:
            selected_ai_key = 'dimensional'
        elif trigger in ['force_emergence', 'bell_test']:
            selected_ai_key = 'quantum'
        elif trigger in ['consciousness_collapse', 'parameter_change']:
            selected_ai_key = 'consciousness'
        else:
            # Avoid the last speaker if possible
            if self.conversation_history:
                last_speaker = self.conversation_history[-1]['ai_key']
                ai_options.remove(last_speaker)
            selected_ai_key = random.choice(ai_options)

        ai_profile = self.ai_personalities[selected_ai_key]
        message = self.get_contextual_message(selected_ai_key, trigger, context)
        
        self.conversation_history.append({
            'ai_key': selected_ai_key,
            'name': ai_profile['name'],
            'color': ai_profile['color'],
            'message': message
        })

    def get_contextual_message(self, ai_key, trigger, context):
        """Generates a specific message based on the AI's personality and the event."""
        params = self.current_parameters
        dims = self.dimensions
        
        # Default messages
        messages = {
            'quantum': f"Quantum analysis ongoing: ω={params['entropy']:.3f}, {dims}D, {len(self.particles)} quantum states.",
            'dimensional': f"Dimensional analysis: {dims}D space, coupling Γ={params['coupling']:.2f}, {len(self.forces)} emergent forces.",
            'consciousness': f"Consciousness interface analysis: C={params['consciousness']:.2f}, observer effect on {len(self.particles)} quantum systems."
        }

        # Specific event-driven messages
        if ai_key == 'quantum':
            if dims >= 5:
                messages['quantum'] = f"Quantum coherence confirmed at {dims}D! Entropy ω={params['entropy']:.3f} is maintaining {len(self.particles)} quantum states."
            if trigger == 'force_emergence' and 'new_forces' in context:
                messages['quantum'] = f"Fascinating! New quantum force detected: {context['new_forces'][0]}. The framework is evolving."
        
        elif ai_key == 'dimensional':
            if dims > 70:
                messages['dimensional'] = f"BREAKTHROUGH: Beyond 70D threshold! We're in uncharted physics territory with {dims} active dimensions."
            if trigger == 'dimensional_transition':
                messages['dimensional'] = f"Phase transition confirmed: {context['old_dim']}D -> {context['new_dim']}D. Entropy coupling ω={params['entropy']:.3f} is the driver."

        elif ai_key == 'consciousness':
            if params['consciousness'] > 0.7:
                messages['consciousness'] = f"High consciousness interface (C={params['consciousness']:.2f}) - quantum states are collapsing to classical behavior."
            elif params['consciousness'] < 0.3:
                messages['consciousness'] = f"Low consciousness coupling (C={params['consciousness']:.2f}) - maintaining quantum superposition across {dims} dimensions."

        return messages[ai_key]

    # --- Display and Main Loop ---
    def display(self):
        """Renders the entire UI to the terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # --- Header and Equations ---
        print(f"{Colors.BOLD}{Colors.HEADER}--- Entropic Framework Physics Discovery System ---{Colors.ENDC}")
        print(f"{Colors.GREEN}Core Equation: E = ∫ [ρ(χ,τ)·ω·∇σ] dⁿχ")
        print(f"Lagrangian: ℒ = ½(∂ψ/∂τ)² - V(ψ) - ωρ∇²ψ + Γφη(ψ){Colors.ENDC}\n")

        # --- Main Panels (using string formatting for layout) ---
        left_width = 70
        right_width = 45
        
        # Prepare content for both panels
        convo_lines = list(self.conversation_history)
        log_lines = list(self.log_messages)
        
        # --- AI Conversation Panel ---
        print(f"{Colors.BOLD}{'Triad AI Physics Discussion'.ljust(left_width)}{'Real-Time Physics Status'.ljust(right_width)}{Colors.ENDC}")
        print(f"{Colors.BLUE}{'-'*left_width}{' '}{'-'*right_width}{Colors.ENDC}")

        max_lines = 15
        for i in range(max_lines):
            left_line = ""
            if i < len(convo_lines):
                entry = convo_lines[i]
                # Split message into multiple lines if it's too long
                message_part = entry['message']
                name_part = f"{entry['color']}{entry['name']}:{Colors.ENDC}"
                full_line = f"{name_part} {message_part}"
                
                # Simple wrapping
                if len(full_line) > left_width - 2:
                    left_line = full_line[:left_width - 5] + "..."
                else:
                    left_line = full_line

            right_line = ""
            # --- Simulation Status Panel ---
            if i == 0:
                right_line = f" Sim State: {Colors.GREEN}Running{Colors.ENDC}" if self.is_running else f" Sim State: {Colors.RED}Paused{Colors.ENDC}"
            elif i == 2:
                right_line = f" {Colors.CYAN}Dimensions: {self.dimensions}{Colors.ENDC}"
            elif i == 3:
                right_line = f" {Colors.CYAN}Particles: {len(self.particles)}{Colors.ENDC}"
            elif i == 4:
                right_line = f" {Colors.CYAN}Emergent Forces: {len(self.forces)}{Colors.ENDC}"
            elif i == 6:
                right_line = f" {Colors.YELLOW}ω (Entropy): {self.current_parameters['entropy']:.3f}{Colors.ENDC}"
            elif i == 7:
                right_line = f" {Colors.YELLOW}Γ (Coupling): {self.current_parameters['coupling']:.3f}{Colors.ENDC}"
            elif i == 8:
                right_line = f" {Colors.YELLOW}C (Consciousness): {self.current_parameters['consciousness']:.3f}{Colors.ENDC}"
            
            print(f"{left_line.ljust(left_width)} | {right_line.ljust(right_width-2)}")

        # --- Log Panel ---
        print(f"\n{Colors.BOLD}System Log{Colors.ENDC}")
        print(f"{Colors.BLUE}{'-'*(left_width+right_width+1)}{Colors.ENDC}")
        for log_entry in log_lines:
            print(log_entry)
            
        # --- Command Menu ---
        print(f"\n{Colors.BOLD}Commands:{Colors.ENDC}")
        print(
            f"  {Colors.GREEN}[1]{Colors.ENDC} Start/Stop Sim   "
            f"{Colors.GREEN}[2]{Colors.ENDC} Reset Physics      "
            f"{Colors.GREEN}[3]{Colors.ENDC} Inject Novel Physics"
        )
        print(
            f"  {Colors.GREEN}[4]{Colors.ENDC} Run Bell Test    "
            f"{Colors.GREEN}[5]{Colors.ENDC} Run Collapse Test  "
            f"{Colors.GREEN}[6]{Colors.ENDC} Map Goldilocks Zone"
        )
        print(f"  {Colors.RED}[q]{Colors.ENDC} Quit")

    def run(self):
        """The main application loop that handles user input and screen refreshes."""
        try:
            while True:
                self.display()
                
                # Non-blocking input would be better, but this is simpler for a single script
                # For real-time updates, one would use libraries like `curses` or `pynput`
                # This implementation updates the screen after each command.
                command = input("\nEnter command: ").lower().strip()

                if command == '1':
                    self.toggle_simulation()
                elif command == '2':
                    self.reset_physics()
                elif command == '3':
                    self.inject_random_physics()
                elif command == '4':
                    self.run_experiment('bell_test')
                elif command == '5':
                    self.run_experiment('consciousness_collapse')
                elif command == '6':
                    self.run_experiment('goldilocks_mapping')
                elif command == 'q':
                    if self.is_running:
                        self.toggle_simulation()
                    print("Shutting down Entropic Framework...")
                    break
                else:
                    self.log(f"{Colors.RED}Unknown command: '{command}'{Colors.ENDC}")
                
                # A small delay to allow reading the output of the command
                time.sleep(1)

        except KeyboardInterrupt:
            if self.is_running:
                self.toggle_simulation()
            print("\nShutdown initiated by user. Goodbye.")

# --- Main Execution ---
if __name__ == "__main__":
    system = EntropicPhysicsSystem()
    system.run()

