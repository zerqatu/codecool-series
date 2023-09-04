from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def most_rated_shows(page_number, order_by, order_type):
    return data_manager.execute_select(f'''
    select s.id as id, title, extract(year from year)::integer as year, runtime, round(rating,1) as rating, string_agg(g.name, ', ' order by g.name) as genres, trailer, homepage
    from shows s
    inner join show_genres sg on s.id = show_id
    inner join genres g on sg.genre_id = g.id
    group by title, year, runtime, rating, trailer, homepage, s.id
    order by {order_by} {order_type}
    limit 15
    offset {page_number} * 15
    ''')


def show_details(show_id):
    query = f'''
    select title,
    extract(year from year)::integer           as year,
    runtime,
    round(rating, 1)                           as rating,
    overview,
    trailer,
    string_agg(genres.name, ', ')     as genres,
    (select string_agg(show_actors.name, ', ')
    from (select a.name from shows s 
    join show_characters sc on s.id = sc.show_id
    join actors a on sc.actor_id = a.id
    where s.id = '{show_id}'
    group by s.id, a.name
    limit 3) as show_actors) as top_actors
    from shows s,
    (select sg.show_id as show_id, name
    from genres g
    join show_genres sg on g.id = sg.genre_id) as genres
    where s.id = '{show_id}'
    and s.id = genres.show_id
    group by title, year, runtime, rating, overview, trailer;
    '''
    return data_manager.execute_select(query, fetchall=False)


def get_seasons(show_id):
    return data_manager.execute_select(f'''
    select season_number, se.title, se.overview
    from seasons se
    join shows s
    on s.id = se.show_id
    where s.id = '{show_id}'
    order by se.season_number;
    ''')


def get_avg_ratings():
    return data_manager.execute_select('''
    select title,
    count(a.name)                as actor_count,
    round(rating, 2)             as rating,
    average,
    round((rating - average), 2) as difference
    from shows s
    join show_characters sc on s.id = sc.show_id
    join actors a on a.id = sc.actor_id
    cross join
    (select avg(rating) as average
    from shows) as avg_rating
    group by title, rating, avg_rating.average
    order by actor_count desc
    limit 10;
    ''')


def get_all_ordered_shows():
    asc = get_ordered_shows("asc")
    desc = get_ordered_shows("desc")
    return asc, desc


def get_ordered_shows(order):
    return data_manager.execute_select(f'''
select s.title, round(rating) as rating, count(e.id) as episode_count
from shows s
join seasons se on s.id = se.show_id
join episodes e on se.id = e.season_id
group by s.title, rating
order by episode_count {order}
limit 10;
    ''')


def get_birthday_actors():
    return data_manager.execute_select('''
    select name, extract(day from birthday)::integer as day
    from actors
    where death is null
    order by birthday
    limit 100;
    ''')


def get_actors():
    return data_manager.execute_select('''
    select id, split_part(name, ' ', 1)as name
    from actors
    order by birthday
    limit 100;''')


def get_shows_by_actor(actor_id):
    return data_manager.execute_select(f'''
    select s.title
    from shows s
    join show_characters sc on s.id = sc.show_id
    join actors a on sc.actor_id = a.id
    where a.id = {actor_id}''')


def count_entries():
    return data_manager.execute_select('''
    select s.id as id, string_agg(g.name, ', ' order by g.name) as genres
    from shows s
    inner join show_genres sg on s.id = show_id
    inner join genres g on sg.genre_id = g.id
    group by s.id
    ''')


def common_characters():
    return data_manager.execute_select('''
    select sc.character_name, count(sc.character_name) as count
    from shows s
    join show_characters sc on s.id = sc.show_id
    where sc.character_name not like 'Himself%'
      and sc.character_name not like 'Herself%'
    and sc.character_name not like 'Host%'
    and sc.character_name not like 'Narrator%'
    group by character_name
    having length(sc.character_name) > 1
    order by count desc
    limit 25;
    ''')


def shows_by_character(character_name):
    return data_manager.execute_select(f'''
    select string_agg(distinct title, ', ') as show
    from shows s
    join show_characters sc on s.id = sc.show_id
    where sc.character_name = '{character_name}';
    ''')

