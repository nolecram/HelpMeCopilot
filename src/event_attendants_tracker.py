#!/usr/bin/env python3
"""
Event Attendants Tracking Application
Track attendants across multiple events with check-in/check-out functionality
"""

# Importazione dei moduli necessari per gestione date e annotazioni di tipo
from datetime import datetime
from typing import Dict, List, Optional, Set


class Attendant:
    """Rappresenta un partecipante all'evento con le sue informazioni personali"""
    
    def __init__(self, attendant_id: str, name: str, email: str, phone: str = ""):
        """
        Inizializza un partecipante
        
        Args:
            attendant_id: Identificatore univoco del partecipante
            name: Nome completo del partecipante
            email: Indirizzo email
            phone: Numero di telefono (opzionale)
        """
        # Memorizza le informazioni personali del partecipante
        self.attendant_id = attendant_id
        self.name = name
        self.email = email
        self.phone = phone
        # Set degli ID degli eventi a cui il partecipante è registrato
        self.events_registered: Set[str] = set()
    
    def __str__(self):
        return f"Attendant({self.attendant_id}, {self.name}, {self.email})"
    
    def __repr__(self):
        return self.__str__()


class Event:
    """Rappresenta un evento con funzionalità di tracciamento dei partecipanti"""
    
    def __init__(self, event_id: str, name: str, date: str, location: str, 
                 max_capacity: int = None):
        """
        Inizializza un evento
        
        Args:
            event_id: Identificatore univoco dell'evento
            name: Nome dell'evento
            date: Data dell'evento (formato: YYYY-MM-DD)
            location: Luogo dell'evento
            max_capacity: Numero massimo di partecipanti (opzionale)
        """
        # Informazioni di base dell'evento
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location
        self.max_capacity = max_capacity
        # Dizionario dei partecipanti registrati (ID -> oggetto Attendant)
        self.registered_attendants: Dict[str, Attendant] = {}
        # Set degli ID dei partecipanti che hanno effettuato il check-in
        self.checked_in_attendants: Set[str] = set()
        # Set degli ID dei partecipanti che hanno effettuato il check-out
        self.checked_out_attendants: Set[str] = set()
    
    def register_attendant(self, attendant: Attendant) -> bool:
        """
        Registra un partecipante all'evento
        
        Args:
            attendant: Oggetto Attendant da registrare
            
        Returns:
            True se la registrazione ha successo, False altrimenti
        """
        # Verifica se l'evento ha raggiunto la capacità massima
        if self.max_capacity and len(self.registered_attendants) >= self.max_capacity:
            return False
        
        # Verifica se il partecipante è già registrato
        if attendant.attendant_id in self.registered_attendants:
            return False
        
        # Registra il partecipante all'evento
        self.registered_attendants[attendant.attendant_id] = attendant
        attendant.events_registered.add(self.event_id)
        return True
    
    def unregister_attendant(self, attendant_id: str) -> bool:
        """
        Annulla la registrazione di un partecipante dall'evento
        
        Args:
            attendant_id: ID del partecipante da rimuovere
            
        Returns:
            True se l'annullamento ha successo, False altrimenti
        """
        # Verifica che il partecipante sia registrato
        if attendant_id not in self.registered_attendants:
            return False
        
        # Rimuove il partecipante dall'evento
        attendant = self.registered_attendants[attendant_id]
        del self.registered_attendants[attendant_id]
        attendant.events_registered.discard(self.event_id)
        
        # Rimuove il partecipante dalle liste di check-in/out se presente
        self.checked_in_attendants.discard(attendant_id)
        self.checked_out_attendants.discard(attendant_id)
        
        return True
    
    def check_in_attendant(self, attendant_id: str) -> bool:
        """
        Registra l'ingresso di un partecipante all'evento
        
        Args:
            attendant_id: ID del partecipante da registrare in ingresso
            
        Returns:
            True se il check-in ha successo, False altrimenti
        """
        # Verifica che il partecipante sia registrato all'evento
        if attendant_id not in self.registered_attendants:
            return False
        
        # Verifica che il partecipante non abbia già effettuato il check-in
        if attendant_id in self.checked_in_attendants:
            return False
        
        # Registra il check-in del partecipante
        self.checked_in_attendants.add(attendant_id)
        return True
    
    def check_out_attendant(self, attendant_id: str) -> bool:
        """
        Registra l'uscita di un partecipante dall'evento
        
        Args:
            attendant_id: ID del partecipante da registrare in uscita
            
        Returns:
            True se il check-out ha successo, False altrimenti
        """
        # Verifica che il partecipante abbia effettuato il check-in
        if attendant_id not in self.checked_in_attendants:
            return False
        
        # Sposta il partecipante dalla lista check-in alla lista check-out
        self.checked_in_attendants.remove(attendant_id)
        self.checked_out_attendants.add(attendant_id)
        return True
    
    def get_attendant_status(self, attendant_id: str) -> Optional[str]:
        """
        Ottiene lo stato di un partecipante per questo evento
        
        Args:
            attendant_id: ID del partecipante
            
        Returns:
            Stringa di stato: 'registered', 'checked_in', 'checked_out', o None
        """
        # Verifica che il partecipante sia registrato
        if attendant_id not in self.registered_attendants:
            return None
        
        # Determina lo stato corrente del partecipante
        if attendant_id in self.checked_out_attendants:
            return 'checked_out'
        elif attendant_id in self.checked_in_attendants:
            return 'checked_in'
        else:
            return 'registered'
    
    def get_statistics(self) -> Dict[str, int]:
        """
        Ottiene le statistiche dell'evento
        
        Returns:
            Dizionario con il conteggio di registrazioni, check-in e check-out
        """
        return {
            'total_registered': len(self.registered_attendants),
            'checked_in': len(self.checked_in_attendants),
            'checked_out': len(self.checked_out_attendants),
            # Calcola il numero di partecipanti registrati ma non ancora entrati
            'not_checked_in': len(self.registered_attendants) - len(self.checked_in_attendants) - len(self.checked_out_attendants),
            # Calcola la capacità rimanente se presente un limite
            'capacity_remaining': (self.max_capacity - len(self.registered_attendants)) if self.max_capacity else None
        }
    
    def __str__(self):
        return f"Event({self.event_id}, {self.name}, {self.date}, {self.location})"
    
    def __repr__(self):
        return self.__str__()


class EventTracker:
    """Classe principale per tracciare i partecipanti attraverso più eventi"""
    
    def __init__(self):
        """Inizializza l'EventTracker"""
        # Dizionario di tutti gli eventi (ID evento -> oggetto Event)
        self.events: Dict[str, Event] = {}
        # Dizionario di tutti i partecipanti (ID partecipante -> oggetto Attendant)
        self.attendants: Dict[str, Attendant] = {}
    
    def create_event(self, event_id: str, name: str, date: str, 
                     location: str, max_capacity: int = None) -> bool:
        """
        Crea un nuovo evento
        
        Args:
            event_id: Identificatore univoco dell'evento
            name: Nome dell'evento
            date: Data dell'evento (formato: YYYY-MM-DD)
            location: Luogo dell'evento
            max_capacity: Numero massimo di partecipanti (opzionale)
            
        Returns:
            True se l'evento è creato con successo, False se l'event_id esiste già
        """
        # Verifica che l'ID evento non esista già
        if event_id in self.events:
            return False
        
        # Crea e memorizza il nuovo evento
        self.events[event_id] = Event(event_id, name, date, location, max_capacity)
        return True
    
    def create_attendant(self, attendant_id: str, name: str, 
                        email: str, phone: str = "") -> bool:
        """
        Crea un nuovo partecipante
        
        Args:
            attendant_id: Identificatore univoco del partecipante
            name: Nome completo del partecipante
            email: Indirizzo email
            phone: Numero di telefono (opzionale)
            
        Returns:
            True se il partecipante è creato con successo, False se l'attendant_id esiste già
        """
        # Verifica che l'ID partecipante non esista già
        if attendant_id in self.attendants:
            return False
        
        # Crea e memorizza il nuovo partecipante
        self.attendants[attendant_id] = Attendant(attendant_id, name, email, phone)
        return True
    
    def register_attendant_to_event(self, attendant_id: str, event_id: str) -> bool:
        """
        Registra un partecipante a un evento
        
        Args:
            attendant_id: ID del partecipante
            event_id: ID dell'evento
            
        Returns:
            True se la registrazione ha successo, False altrimenti
        """
        # Verifica che sia il partecipante che l'evento esistano
        if attendant_id not in self.attendants or event_id not in self.events:
            return False
        
        # Delega la registrazione all'oggetto Event
        return self.events[event_id].register_attendant(self.attendants[attendant_id])
    
    def get_attendant_events(self, attendant_id: str) -> List[Event]:
        """
        Ottiene tutti gli eventi a cui un partecipante è registrato
        
        Args:
            attendant_id: ID del partecipante
            
        Returns:
            Lista di oggetti Event
        """
        # Verifica che il partecipante esista
        if attendant_id not in self.attendants:
            return []
        
        # Recupera la lista degli eventi a cui il partecipante è registrato
        attendant = self.attendants[attendant_id]
        return [self.events[event_id] for event_id in attendant.events_registered 
                if event_id in self.events]
    
    def get_event_attendants(self, event_id: str) -> List[Attendant]:
        """
        Ottiene tutti i partecipanti registrati a un evento
        
        Args:
            event_id: ID dell'evento
            
        Returns:
            Lista di oggetti Attendant
        """
        # Verifica che l'evento esista
        if event_id not in self.events:
            return []
        
        # Restituisce la lista di tutti i partecipanti registrati
        return list(self.events[event_id].registered_attendants.values())
    
    def search_attendants(self, query: str) -> List[Attendant]:
        """
        Cerca i partecipanti per nome o email
        
        Args:
            query: Stringa di ricerca
            
        Returns:
            Lista di oggetti Attendant corrispondenti
        """
        # Verifica che la query non sia vuota
        if not query or not query.strip():
            return []
        
        query_lower = query.lower()
        results = []
        
        # Cerca nei nomi e nelle email dei partecipanti
        for attendant in self.attendants.values():
            if (query_lower in attendant.name.lower() or 
                query_lower in attendant.email.lower()):
                results.append(attendant)
        
        return results
    
    def search_events(self, query: str) -> List[Event]:
        """
        Cerca gli eventi per nome o luogo
        
        Args:
            query: Stringa di ricerca
            
        Returns:
            Lista di oggetti Event corrispondenti
        """
        # Verifica che la query non sia vuota
        if not query or not query.strip():
            return []
        
        query_lower = query.lower()
        results = []
        
        # Cerca nei nomi e nei luoghi degli eventi
        for event in self.events.values():
            if (query_lower in event.name.lower() or 
                query_lower in event.location.lower()):
                results.append(event)
        
        return results
    
    def get_all_events(self) -> List[Event]:
        """Ottiene tutti gli eventi"""
        return list(self.events.values())
    
    def get_all_attendants(self) -> List[Attendant]:
        """Ottiene tutti i partecipanti"""
        return list(self.attendants.values())


def display_event_details(event: Event):
    """Visualizza informazioni dettagliate su un evento"""
    print(f"\n{'='*70}")
    print(f"📅 EVENT: {event.name}")
    print(f"{'='*70}")
    print(f"Event ID: {event.event_id}")
    print(f"Date: {event.date}")
    print(f"Location: {event.location}")
    # Mostra la capacità o il numero di registrati
    if event.max_capacity:
        print(f"Capacity: {len(event.registered_attendants)}/{event.max_capacity}")
    else:
        print(f"Registered: {len(event.registered_attendants)}")
    
    # Recupera e mostra le statistiche dell'evento
    stats = event.get_statistics()
    print(f"\n📊 STATISTICS:")
    print(f"  Total Registered: {stats['total_registered']}")
    print(f"  Checked In: {stats['checked_in']}")
    print(f"  Checked Out: {stats['checked_out']}")
    print(f"  Not Yet Checked In: {stats['not_checked_in']}")
    if stats['capacity_remaining'] is not None:
        print(f"  Capacity Remaining: {stats['capacity_remaining']}")
    
    # Mostra la lista dei partecipanti con il loro stato
    if event.registered_attendants:
        print(f"\n👥 ATTENDANTS:")
        print("-" * 70)
        for attendant_id, attendant in event.registered_attendants.items():
            status = event.get_attendant_status(attendant_id)
            # Mappa lo stato a un emoji appropriato
            status_emoji = {
                'registered': '📝',
                'checked_in': '✅',
                'checked_out': '👋'
            }.get(status, '❓')
            print(f"  {status_emoji} {attendant.name} ({attendant.email}) - {status.upper()}")
    print("=" * 70)


def display_attendant_details(attendant: Attendant, tracker: EventTracker):
    """Visualizza informazioni dettagliate su un partecipante"""
    print(f"\n{'='*70}")
    print(f"👤 ATTENDANT: {attendant.name}")
    print(f"{'='*70}")
    print(f"ID: {attendant.attendant_id}")
    print(f"Email: {attendant.email}")
    if attendant.phone:
        print(f"Phone: {attendant.phone}")
    
    # Recupera tutti gli eventi a cui il partecipante è registrato
    events = tracker.get_attendant_events(attendant.attendant_id)
    print(f"\n📅 REGISTERED EVENTS ({len(events)}):")
    print("-" * 70)
    
    # Mostra la lista degli eventi con il relativo stato
    if events:
        for event in events:
            status = event.get_attendant_status(attendant.attendant_id)
            # Mappa lo stato a un emoji appropriato
            status_emoji = {
                'registered': '📝',
                'checked_in': '✅',
                'checked_out': '👋'
            }.get(status, '❓')
            print(f"  {status_emoji} {event.name} - {event.date} ({event.location}) - {status.upper()}")
    else:
        print("  No events registered")
    print("=" * 70)


def main():
    """Funzione principale per eseguire l'applicazione di tracciamento partecipanti agli eventi"""
    tracker = EventTracker()
    
    # Dati di esempio per dimostrazione
    print("🎫 Event Attendants Tracking System 🎫")
    print("=" * 60)
    print("\nInitializing with sample data...")
    
    # Crea eventi di esempio
    tracker.create_event("evt001", "Python Conference 2025", "2025-03-15", "San Francisco", 100)
    tracker.create_event("evt002", "Tech Meetup", "2025-04-20", "New York", 50)
    tracker.create_event("evt003", "DevOps Workshop", "2025-05-10", "Austin")
    
    # Crea partecipanti di esempio
    tracker.create_attendant("att001", "Alice Johnson", "alice@email.com", "555-0101")
    tracker.create_attendant("att002", "Bob Smith", "bob@email.com", "555-0102")
    tracker.create_attendant("att003", "Carol Williams", "carol@email.com", "555-0103")
    tracker.create_attendant("att004", "David Brown", "david@email.com", "555-0104")
    
    # Registra i partecipanti agli eventi
    tracker.register_attendant_to_event("att001", "evt001")
    tracker.register_attendant_to_event("att001", "evt002")
    tracker.register_attendant_to_event("att002", "evt001")
    tracker.register_attendant_to_event("att002", "evt003")
    tracker.register_attendant_to_event("att003", "evt001")
    tracker.register_attendant_to_event("att004", "evt002")
    
    # Effettua il check-in di alcuni partecipanti
    tracker.events["evt001"].check_in_attendant("att001")
    tracker.events["evt001"].check_in_attendant("att002")
    tracker.events["evt002"].check_in_attendant("att001")
    
    # Effettua il check-out di un partecipante
    tracker.events["evt001"].check_out_attendant("att001")
    
    print("Sample data loaded successfully!\n")
    
    while True:
        print("\n" + "="*60)
        print("MAIN MENU")
        print("="*60)
        print("1. View all events")
        print("2. View event details")
        print("3. View all attendants")
        print("4. View attendant details")
        print("5. Create new event")
        print("6. Create new attendant")
        print("7. Register attendant to event")
        print("8. Check in attendant")
        print("9. Check out attendant")
        print("10. Search events")
        print("11. Search attendants")
        print("12. Exit")
        print("="*60)
        
        try:
            choice = input("Enter your choice (1-12): ").strip()
            
            if choice == "1":
                # Visualizza tutti gli eventi
                events = tracker.get_all_events()
                if events:
                    print(f"\n📅 ALL EVENTS ({len(events)}):")
                    print("-" * 60)
                    for event in events:
                        stats = event.get_statistics()
                        print(f"  {event.event_id}: {event.name}")
                        print(f"    Date: {event.date} | Location: {event.location}")
                        print(f"    Registered: {stats['total_registered']} | Checked In: {stats['checked_in']}")
                else:
                    print("\nNo events found.")
            
            elif choice == "2":
                # Visualizza dettagli evento
                event_id = input("Enter event ID: ").strip()
                if event_id in tracker.events:
                    display_event_details(tracker.events[event_id])
                else:
                    print("Event not found!")
            
            elif choice == "3":
                # Visualizza tutti i partecipanti
                attendants = tracker.get_all_attendants()
                if attendants:
                    print(f"\n👥 ALL ATTENDANTS ({len(attendants)}):")
                    print("-" * 60)
                    for attendant in attendants:
                        events_count = len(attendant.events_registered)
                        print(f"  {attendant.attendant_id}: {attendant.name}")
                        print(f"    Email: {attendant.email} | Events: {events_count}")
                else:
                    print("\nNo attendants found.")
            
            elif choice == "4":
                # Visualizza dettagli partecipante
                attendant_id = input("Enter attendant ID: ").strip()
                if attendant_id in tracker.attendants:
                    display_attendant_details(tracker.attendants[attendant_id], tracker)
                else:
                    print("Attendant not found!")
            
            elif choice == "5":
                # Crea nuovo evento
                print("\n--- Create New Event ---")
                event_id = input("Event ID: ").strip()
                name = input("Event Name: ").strip()
                date = input("Date (YYYY-MM-DD): ").strip()
                location = input("Location: ").strip()
                capacity_input = input("Max Capacity (press Enter for unlimited): ").strip()
                
                # Converte la capacità in intero, se fornita
                max_capacity = None
                if capacity_input:
                    try:
                        max_capacity = int(capacity_input)
                    except ValueError:
                        print("Invalid capacity. Setting to unlimited.")
                
                if tracker.create_event(event_id, name, date, location, max_capacity):
                    print(f"✅ Event '{name}' created successfully!")
                else:
                    print("❌ Event ID already exists!")
            
            elif choice == "6":
                # Crea nuovo partecipante
                print("\n--- Create New Attendant ---")
                attendant_id = input("Attendant ID: ").strip()
                name = input("Name: ").strip()
                email = input("Email: ").strip()
                phone = input("Phone (optional): ").strip()
                
                if tracker.create_attendant(attendant_id, name, email, phone):
                    print(f"✅ Attendant '{name}' created successfully!")
                else:
                    print("❌ Attendant ID already exists!")
            
            elif choice == "7":
                # Registra partecipante a evento
                attendant_id = input("Enter attendant ID: ").strip()
                event_id = input("Enter event ID: ").strip()
                
                if tracker.register_attendant_to_event(attendant_id, event_id):
                    print("✅ Attendant registered successfully!")
                else:
                    print("❌ Registration failed! Check IDs or event capacity.")
            
            elif choice == "8":
                # Effettua check-in partecipante
                event_id = input("Enter event ID: ").strip()
                attendant_id = input("Enter attendant ID: ").strip()
                
                if event_id in tracker.events:
                    if tracker.events[event_id].check_in_attendant(attendant_id):
                        print("✅ Attendant checked in successfully!")
                    else:
                        print("❌ Check-in failed! Attendant may not be registered or already checked in.")
                else:
                    print("❌ Event not found!")
            
            elif choice == "9":
                # Effettua check-out partecipante
                event_id = input("Enter event ID: ").strip()
                attendant_id = input("Enter attendant ID: ").strip()
                
                if event_id in tracker.events:
                    if tracker.events[event_id].check_out_attendant(attendant_id):
                        print("✅ Attendant checked out successfully!")
                    else:
                        print("❌ Check-out failed! Attendant may not be checked in.")
                else:
                    print("❌ Event not found!")
            
            elif choice == "10":
                # Cerca eventi
                query = input("Enter search query (name or location): ").strip()
                results = tracker.search_events(query)
                
                if results:
                    print(f"\n🔍 Found {len(results)} event(s):")
                    print("-" * 60)
                    for event in results:
                        print(f"  {event.event_id}: {event.name} - {event.date} ({event.location})")
                else:
                    print("No events found matching your query.")
            
            elif choice == "11":
                # Cerca partecipanti
                query = input("Enter search query (name or email): ").strip()
                results = tracker.search_attendants(query)
                
                if results:
                    print(f"\n🔍 Found {len(results)} attendant(s):")
                    print("-" * 60)
                    for attendant in results:
                        print(f"  {attendant.attendant_id}: {attendant.name} ({attendant.email})")
                else:
                    print("No attendants found matching your query.")
            
            elif choice == "12":
                print("\n" + "="*60)
                print("Thank you for using Event Attendants Tracking System! 🎫")
                print("="*60)
                break
            
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 12.")
        
        except KeyboardInterrupt:
            print("\n\n" + "="*60)
            print("Thank you for using Event Attendants Tracking System! 🎫")
            print("="*60)
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
