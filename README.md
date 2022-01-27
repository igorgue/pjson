pjson
=====

JSON formatting but with moar colors (and less conf)

### Usage

```sh
echo '{"json":"obj"}' | pjson
```

```json
{
  "json": "obj"
}
```

### Looks Like This

Image for the haters:

![Screenshot-20220126190421-653x680](https://user-images.githubusercontent.com/7014/151272641-de8dfbb9-7f49-4f59-89f2-cc4c1b6afb55.png)

Small retina display images are fucking huge.

### Example With Curl

```sh
curl https://api.github.com/users/igorgue | pjson
```

### Install

Install `pygments` and `xmlformatter`:

```sh
pip install pjson xmlformatter
```

### MFW I did This Project

![image](http://1.bp.blogspot.com/-pPlP3YNu_8E/U5lOw22806I/AAAAAAAAIwA/gbpKuF4RerA/s1600/puking_rainbows_guy_in_hd_by_lemmino-d6026ug.png)
